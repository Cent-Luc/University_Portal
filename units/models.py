from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
class Unit(models.Model):
    title = models.CharField(max_length=200)
    code = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       on_delete=models.CASCADE,
)  
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('unit_detail', args=[str(self.id)])

    SEMESTER_JOINED_CHOICES = [
        ("Jan-Apr", "Jan - Apr"),
        ("May-Aug", "May - Aug"),
        ("Sept-Dec", "Sept - Dec"),
]
    year_joined = models.IntegerField(default=int(datetime.now().year))
    semester_joined = models.CharField(
        max_length=15,
        choices=SEMESTER_JOINED_CHOICES
)
