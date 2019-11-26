from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import StudentFeePayment

class StudentFeePaymentCreateView(CreateView):
    model = StudentFeePayment
    fields = ("student", "learning_year", "learning_semester", "fee_amount")
    template_name = 'StudentFeePayment_create.html'
    success_url = reverse_lazy('StudentFeePayment_list')

class StudentFeePaymentListView(ListView):
    model = StudentFeePayment
    template_name = 'StudentFeePayment_list.html'

class StudentFeePaymentDetailView(DetailView):
    model = StudentFeePayment
    template_name = 'StudentFeePayment_detail.html'

class StudentFeePaymentUpdateView(UpdateView):
    model = StudentFeePayment
    template_name = 'StudentFeePayment_edit.html'
            