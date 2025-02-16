from django import forms
from .models import BespokeRequest


class BespokeRequestForm(forms.ModelForm):

    class Meta:
        model = BespokeRequest
        fields = ['name', 'telephonenumber', 'email', 'message']
