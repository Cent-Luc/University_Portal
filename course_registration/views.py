from braces.views import (
    LoginRequiredMixin,
    SuperuserRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import CourseRegistration
from students.models import Student

class CourseRegistrationView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CourseRegistration
    template_name = "add.html"
    fields = ('course', 'learning_year', 'learning_semester')
    login_url = "student_detail"

    def test_func(self, user):
        return (Student.objects.filter(user=user).exists())

    def form_valid(self, form):
        """
        Overridden to always set the user field to the currently logged in user
        """
        user = self.request.user
        form.instance.student = Student.objects.filter(user=user).first()
        return super(CourseRegistrationView, self).form_valid(form)

class CourseRegistrationUpdateView(LoginRequiredMixin, UpdateView):
    model = CourseRegistration
    fields = ('user', 'category', 'is_verified')
    template_name = "update.html"

class CourseRegistrationDetailView(LoginRequiredMixin, DetailView):
    model = CourseRegistration
    template_name = "detail.html"

class CourseRegistrationListView(LoginRequiredMixin, ListView):
    model = CourseRegistration
    template_name = 'list.html'
    ordering = ['-learning_year', 'learning_semester']

    def get_queryset(self):
        student = Student.objects.filter(user=self.request.user).first()
        return super().get_queryset().filter(student=student)

class CRStaffListView(LoginRequiredMixin, ListView):
    model = CourseRegistration
    template_name = 'list.html'
    ordering = ['is_verified', 'user__email']
