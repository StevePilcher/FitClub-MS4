from django import forms
from .models import Review


class NewReviewForm(forms.ModelForm):
    message = forms.CharField(max_length=500)

    class Meta:
        model = Review
        fields = ['review_title', 'review_description']
