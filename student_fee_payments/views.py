from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.urls import reverse_lazy

from .models import StudentFeePayment

class StudentFeePaymentCreateView(CreateView):
    model = StudentFeePayment
    fields = ("student", "learning_year", "learning_semester", "fee_amount")
    template_name = 'student_fee_payments/add.html'

class StudentFeePaymentListView(ListView):
    model = StudentFeePayment
    template_name = 'student_fee_payments/list.html'
    ordering = ['-learning_year', 'learning_semester', 'student__user__email']

# class StudentFeePaymentDetailView(DetailView):
    # model = StudentFeePayment
    # template_name = 'student_fee_payments/detail.html'

class StudentFeePaymentUpdateView(UpdateView):
    model = StudentFeePayment
    fields = ("learning_year", "learning_semester", "fee_amount")
    template_name = 'student_fee_payments/edit.html'
