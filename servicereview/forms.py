from django import forms
from .models import ServiceReview


class ServiceReviewForm(forms.ModelForm):

    class Meta:
        model = ServiceReview
        fields = ['name', 'email', 'review']
