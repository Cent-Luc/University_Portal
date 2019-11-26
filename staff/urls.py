from django.urls import path

from .views import (
    StaffRegistrationView,
    StaffUpdateView,
    StaffDetailView,
)

urlpatterns = [
    path("<int:pk>/edit/",
         StaffUpdateView.as_view(),
         name="staff_edit"),
    path("<int:pk>/",
         StaffDetailView.as_view(),
         name="staff_detail"),
    path("new/",
         StaffRegistrationView.as_view(),
         name="staff_new"),
]
