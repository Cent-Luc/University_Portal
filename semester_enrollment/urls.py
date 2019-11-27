from django.urls import path

from .views import (
    SemesterEnrollmentCreateView,
    SemesterEnrollmentUpdateView,
    SemesterEnrollmentListView,
    SemesterEnrollmentDetailView,
)

urlpatterns = [
    path("<int:pk>/edit/",
         SemesterEnrollmentUpdateView.as_view(),
         name="sem_enroll_edit"),
    path("<int:pk>/",
         SemesterEnrollmentDetailView.as_view(),
         name="sem_enroll_detail"),
    path("new/<int:course_reg_pk>/",
         SemesterEnrollmentCreateView.as_view(),
         name="sem_enroll_new"),
    path("",
         SemesterEnrollmentListView.as_view(),
         name="sem_enroll_list"),
]
