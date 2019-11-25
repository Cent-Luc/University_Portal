from django import forms
from courses.models import Course
from students.models import Student

class StudentEnrollForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all(),
                                     widget=forms.HiddenInput)
class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)
