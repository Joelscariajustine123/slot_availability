# booking/models.py

from django.db import models

# Define the course model
class Course(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Define the slot model

class Slot(models.Model):
    # Define the timing field for the slot
    timing = models.CharField(max_length=100)
    batch = models.CharField(max_length=50)
    student_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.timing} ({self.batch})"

# Define the student model
class Student(models.Model):
    gcard_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
