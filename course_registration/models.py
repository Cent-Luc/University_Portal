from django.db import models
from students.models import Student
from courses.models import Course
from datetime import datetime

class CourseRegistration(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    semester = [
        ("Jan-Apr", "Jan - Apr"),
        ("May-Aug", "May - Aug"),
        ("Sept-Dec", "Sept - Dec"),
    ]
    learning_year = models.IntegerField('Year of Study', default=int(datetime.now().year))
    learning_semester = models.CharField('Semester of Study' ,
        max_length=15,
        choices=semester
    )

# Create your models here.
