from django import forms
from .models import Review


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('sku', 'review_user')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'Review Title',
            'review_desc': 'Review',
            'rating': 'Rating',
            'review_date': 'Date',
        }
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder

