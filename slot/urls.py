from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('slot_availability/', views.slot_availability, name='slot_availability'),
    path('course_wise_list/', views.course_wise_list, name='course_wise_list'),
    path('add_course/', views.add_course, name='add_course'),
    path('remove_student/<int:student_id>/', views.remove_student, name='remove_student'),
    path('remove_course/<int:course_id>/', views.remove_course, name='remove_course'),
]