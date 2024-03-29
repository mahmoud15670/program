from django import forms
from .models import *

class Patient_form(forms.ModelForm):
    mode = Patient
    fields ='__all__'
