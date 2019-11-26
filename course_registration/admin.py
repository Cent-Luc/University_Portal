from django.contrib import admin
from .models import CourseRegistration

class CourseRegistrationAdmin(admin.ModelAdmin):
    model = CourseRegistration
    list_display = ['student','course','learning_semester','learning_year',]

admin.site.register(CourseRegistration,CourseRegistrationAdmin)    

# Register your models here.
