from django.urls import path
from . import views

urlpatterns = [
    path('register/',
        views.UnitRegistrationView.as_view(),
        name='unit_registration'),
    path('enroll-unit/',
         views.UnitEnrollView.as_view(),
         name='student_enroll_unit'),
]
