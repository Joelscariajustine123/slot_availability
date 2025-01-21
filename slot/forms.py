# booking/forms.py

from django import forms
from .models import Student, Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['gcard_id', 'name', 'course', 'slot']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
