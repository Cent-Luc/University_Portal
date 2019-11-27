"""university_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('courses_admin/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('staff/', include('staff.urls')),
    path('fees/', include('student_fee_payments.urls')),
    path('units/', include('units.urls')),
    path('course_reg/', include('course_registration.urls')),
    path('sem_enroll/', include('semester_enrollment.urls')),
    path('', include('home.urls')),
]
