from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UnitEnrollForm

class UnitEnrollView(LoginRequiredMixin, FormView):
    unit = None
    form_class = UnitEnrollForm
    
    def form_valid(self, form):
        self.unit  = form.cleaned_data['unit']
        self.unit.units.add(self.request.user)
        return super(UnitEnrollView,
                     self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_unit_detail',
                            args=[self.unit.id])

class UnitRegistrationView(CreateView):
    template_name = 'units/unit/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('units_unit_list')

    def form_valid(self, form):
        result = super(UnitRegistrationView,
                       self).form_valid(form)
        cd = form.cleaned_data
        user - authenticate(username=cd['username'],
                password=cd['password1'])
        login(self.request, user)
        return result
