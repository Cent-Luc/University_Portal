from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=200)
    code  = models.SlugField(max_length=200, unique=True)
    summary = models.TextField(blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Unit(models.Model):
    course = models.ForeignKey(Course,
                               related_name='courses',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    code = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['created']

    def __str__(self):
        return self.title




class Module(models.Model):
    unit = models.ForeignKey(Unit,
                             related_name='modules',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

