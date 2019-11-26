from django import forms
from units.models import Unit

class UnitEnrollForm(forms.Form):
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(),
                                  widget=forms.HiddenInput)
