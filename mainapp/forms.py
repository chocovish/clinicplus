from .models import Patient,VisitDetail

#from django.forms import ModelForm
from django import forms

class PatientAddForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = []

class AddVisitDetailForm(forms.ModelForm):
    class Meta:
        model = VisitDetail
        exclude = ['patient']

