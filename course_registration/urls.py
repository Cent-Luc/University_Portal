from django.urls import path

from .views import (
    CourseRegistrationView,
    CourseRegistrationUpdateView,
    CourseRegistrationDetailView,
    CourseRegistrationListView,
)

urlpatterns = [
    path("<int:pk>/edit/",
         CourseRegistrationUpdateView.as_view(),
         name="coursereg_edit"),
    path("<int:pk>/",
         CourseRegistrationDetailView.as_view(),
         name="coursereg_detail"),
    path("new/",
         CourseRegistrationView.as_view(),
         name="coursereg_new"),
    path("",
         CourseRegistrationListView.as_view(),
         name="coursereg_list"),
]
