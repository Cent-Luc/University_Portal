from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Staff

class StaffRegistrationView(CreateView):
    model = Staff
    template_name = "staff/registration.html"
    fields = ('national_id', 'category')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(StaffRegistrationView, self).form_valid(form)

class StaffUpdateView(UpdateView):
    pass

class StaffDetailView(DetailView):
    pass
