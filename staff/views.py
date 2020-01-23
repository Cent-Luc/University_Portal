from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Staff

class StaffRegistrationView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Staff
    template_name = "staff/registration.html"
    fields = ('user', 'category', 'is_verified')
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class StaffUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Staff
    fields = ('user', 'category', 'is_verified')
    template_name = "staff/update.html"
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class StaffDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Staff
    template_name = "staff/detail.html"
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser

class StaffVerificationView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Staff
    fields = ('user', 'category', 'is_verified')
    template_name = "staff/verify.html"
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser
    
    def get_success_url(self):
        return reverse_lazy("staff_list")

class StaffListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Staff
    template_name = 'staff/list.html'
    ordering = ['is_verified', 'user__email']
    login_url = 'login'

    def test_func(self):
        return self.request.user.is_superuser
