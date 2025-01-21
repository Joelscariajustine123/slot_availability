# booking/admin.py

from django.contrib import admin
from .models import Student, Course, Slot

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Slot)
