from django import forms
from .models import *

class Patient_form(forms.ModelForm):
    class Meta:
        model = Patient
        fields ='__all__'
