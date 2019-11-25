from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=13, unique=True)
    level_of_study = models.CharField(max_length=200)
    sponsor = models.CharField(max_length=200)
    year_joined = models.DateTimeField(auto_now_add=True)
    semester_joined = models.CharField(max_length=200)
    national_id = models.IntegerField(unique=True)
    date_of_birth = models.DateTimeField
    nhif_owner = models.CharField(max_length=200)
    nhif_membership_no = models.IntegerField(unique=True)
    is_card_valid = models.BooleanField
    valid_until = models.DateTimeField(auto_now_add=True)

