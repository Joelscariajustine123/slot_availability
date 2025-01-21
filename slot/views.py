# booking/views.py

from django.shortcuts import render, redirect
from .models import Student, Course, Slot
from .forms import StudentForm, CourseForm

# View for the home page
def home(request):
    return render(request, 'home.html')

# Register a student
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            slot = student.slot
            slot.student_count += 1
            slot.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'register_student.html', {'form': form})

# View all students in a particular slot
def slot_availability(request):
    slots = Slot.objects.all()
    # Calculate available seats for each slot
    for slot in slots:
        slot.available_seats = 20 - slot.student_count  # Calculate available seats
    return render(request, 'slot_availability.html', {'slots': slots})

# View list of students in each slot
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# View course-wise student list
def course_wise_list(request):
    courses = Course.objects.all()
    return render(request, 'course_wise_list.html', {'courses': courses})

# Add new course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_wise_list')
    else:
        form = CourseForm()
    
    return render(request, 'add_course.html', {'form': form})

# Remove a student after the course is over
def remove_student(request, student_id):
    student = Student.objects.get(id=student_id)
    slot = student.slot
    slot.student_count -= 1
    slot.save()
    student.delete()
    return redirect('student_list')

# Remove a course
def remove_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('course_wise_list')
    