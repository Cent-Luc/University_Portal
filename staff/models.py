from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Staff(models.Model):
    CATEGORY_CHOICES = [
        ("Finance", "Finance"),
        ("HOD", "Head of Department"),
        ("Lecturer", "Lecturer"),
        ("Nurse", "Nurse"),
    ]

    national_id = models.IntegerField(unique=True)
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES
    )
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return reverse("staff_detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
