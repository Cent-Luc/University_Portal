from django.contrib import admin
from .models import StudentFeePayment

class StudentFeePaymentAdmin(admin.ModelAdmin):
    model = StudentFeePayment
    list_display = ['student', 'learning_year', 'learning_semester', 'fee_amount']

admin.site.register(StudentFeePayment, StudentFeePaymentAdmin)
