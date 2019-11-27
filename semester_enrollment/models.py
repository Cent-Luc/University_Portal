from django.db import models

from course_registration.models import CourseRegistration
from students.models import Student

from datetime import datetime
from django.urls import reverse

class SemesterEnrollment(models.Model):
    SEMESTER_CHOICES = [
        ("Jan-Apr", "Jan - Apr"),
        ("May-Aug", "May - Aug"),
        ("Sept-Dec", "Sept - Dec"),
    ]

    enrolled_course = models.ForeignKey(
        CourseRegistration,
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    year = models.IntegerField(default=int(datetime.now().year))
    semester = models.CharField(
        max_length=15,
        choices=SEMESTER_CHOICES
    )

    def __str__(self):
        return str(self.year)

    def get_absolute_url(self):
        return reverse("sem_enroll_detail", args=[str(self.id)])
