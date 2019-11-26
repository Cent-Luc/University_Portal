from django.urls import path

from .views import (
    StudentUpdateView,
    StudentDetailView,
    StudentRegistrationView,
    StudentEnrollCourseView,
    StudentCourseListView,
    StudentCourseDetailView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         StudentUpdateView.as_view(),
         name='student_update'),
    path('<int:pk>',
         StudentDetailView.as_view(),
         name='student_detail'),
    path('new/',
         StudentRegistrationView.as_view(),
         name='student_registration'),
    path('enroll-course/',
         StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),
    path('courses/',
         StudentCourseListView.as_view(),
         name='student_course_list'),
    path('course/<pk>/',
         StudentCourseDetailView.as_view(),
         name=' student_course_detail'),
    path('course/<pk>/<module_id>/',
         StudentCourseDetailView.as_view(),
         name='student_course_detail_module'),
]
