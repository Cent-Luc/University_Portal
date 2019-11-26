from django.contrib import admin
from .models import StudentFeePayment

class StudentFeePaymentAdmin(admin.ModelAdmin):
    model = StudentFeePayment
    list_display = ['student_id' ,'semester' ,'learning_year' ,'learning_semester','fee_amount',]

admin.site.register(StudentFeePayment,StudentFeePaymentAdmin) 
# Register your models here.
