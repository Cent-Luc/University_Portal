from django.db import models
from students.models import Student
from courses.models import Course
from datetime import datetime
from django.urls import reverse

class CourseRegistration(models.Model):
    SEMESTER_CHOICES = [
        ("Jan-Apr", "Jan - Apr"),
        ("May-Aug", "May - Aug"),
        ("Sept-Dec", "Sept - Dec"),
    ]
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    learning_year = models.IntegerField('Year Joined', default=int(datetime.now().year))
    learning_semester = models.CharField(
        'Semester Joined',
        max_length=15,
        choices=SEMESTER_CHOICES
    )

    def get_absolute_url(self):
        return reverse("coursereg_list")
