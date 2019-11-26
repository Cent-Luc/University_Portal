from django.db import models
from datetime import datetime
from django.urls import reverse

from students.models import Student

class StudentFeePayment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    semester = [
        ("Jan-Apr", "Jan - Apr"),
        ("May-Aug", "May - Aug"),
        ("Sept-Dec", "Sept - Dec"),
    ]
    learning_year = models.IntegerField('Year of Study', default=int(datetime.now().year))
    learning_semester = models.CharField(
        'Semester of Study',
        max_length=15,
        choices=semester
    )
    fee_amount = models.IntegerField('Amount Paid')

    def get_absolute_url(self):
        return reverse('StudentFeePayment_list')
