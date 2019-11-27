from braces.views import (
    LoginRequiredMixin,
    SuperuserRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import SemesterEnrollment
from students.models import Student
from course_registration.models import CourseRegistration

class SemesterEnrollmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = SemesterEnrollment
    template_name = "semester_enrollment/add.html"
    fields = ('year', 'semester')
    login_url = "student_detail"

    def test_func(self, user):
        """
        Check if the user is student
        """
        return (Student.objects.filter(user=user).exists())

    def dispatch(self, request, *args, **kwargs):
        self.enrolled_course = get_object_or_404(CourseRegistration, pk=kwargs['course_reg_pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.enrolled_course = self.enrolled_course
        student = Student.objects.filter(user=self.request.user).first()
        form.instance.student = student
        return super(SemesterEnrollmentCreateView, self).form_valid(form)

class SemesterEnrollmentUpdateView(LoginRequiredMixin, UpdateView):
    model = SemesterEnrollment
    fields = ('year', 'semester')
    template_name = "semester_enrollment/edit.html"

class SemesterEnrollmentDetailView(LoginRequiredMixin, DetailView):
    model = SemesterEnrollment
    template_name = "semester_enrollment/detail.html"

class SemesterEnrollmentListView(LoginRequiredMixin, ListView):
    model = SemesterEnrollment
    template_name = 'semester_enrollment/list.html'
    ordering = ['-year', '-semester']

    def get_queryset(self):
        student = Student.objects.filter(user=self.request.user).first()
        return super().get_queryset().filter(student=student)

# class CRStaffListView(LoginRequiredMixin, ListView):
    # model = CourseRegistration
    # template_name = 'list.html'
    # ordering = ['is_verified', 'user__email']
