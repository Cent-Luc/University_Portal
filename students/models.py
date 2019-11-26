from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Student(models.Model):
    LEVEL_OF_STUDY_CHOICES = [
        ("Certificate", "Certificate"),
        ("Diploma", "Diploma"),
        ("Degree", "Degree"),
        ("Master", "Master"),
    ]
    SPONSOR_CHOICES = [
        ("Govt", "Government"),
        ("Self", "Self"),
        ("Other", "Other"),
    ]
    SEMESTER_JOINED_CHOICES = [
        ("Jan-Apr", "Jan - Apr"),
        ("May-Aug", "May - Aug"),
        ("Sept-Dec", "Sept - Dec"),
    ]
    NHIF_CARD_OWNER_CHOICES = [
        ("Self", "Self"),
        ("Guardian", "Guardian"),
    ]

    student_id = models.CharField(
        max_length=13,
        unique=True
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )
    level_of_study = models.CharField(
        max_length=15,
        choices=LEVEL_OF_STUDY_CHOICES
    )
    sponsor = models.CharField(
        max_length=15,
        choices=SPONSOR_CHOICES
    )
    year_joined = models.IntegerField(default=int(datetime.now().year))
    semester_joined = models.CharField(
        max_length=15,
        choices=SEMESTER_JOINED_CHOICES
    )
    national_id = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    nhif_owner = models.CharField(
        max_length=15,
        choices=NHIF_CARD_OWNER_CHOICES
    )
    nhif_membership_no = models.IntegerField(unique=True)
    nhif_is_card_valid = models.BooleanField(default=False)
    nhif_valid_until = models.DateField()

    def __str__(self):
        return self.student_id

    def get_absolute_url(self):
        return reverse("student_detail", args=[str(self.id)])
