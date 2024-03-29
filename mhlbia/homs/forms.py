from django import forms
from .models import *

class Patient_form(forms.ModelForm):
    model = Patient
    fields ='__all__'
