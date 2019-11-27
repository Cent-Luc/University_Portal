from braces.views import (
    LoginRequiredMixin,
    SuperuserRequiredMixin,
)
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Staff

class StaffRegistrationView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = Staff
    template_name = "staff/registration.html"
    fields = ('user', 'category', 'is_verified')

class StaffUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Staff
    fields = ('user', 'category', 'is_verified')
    template_name = "staff/update.html"

class StaffDetailView(LoginRequiredMixin, SuperuserRequiredMixin, DetailView):
    model = Staff
    template_name = "staff/detail.html"

class StaffVerificationView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    model = Staff
    fields = ('user', 'category', 'is_verified')
    template_name = "staff/verify.html"
    
    def get_success_url(self):
        return reverse_lazy("staff_list")

class StaffListView(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    model = Staff
    template_name = 'staff/list.html'
    ordering = ['is_verified', 'user__email']
