from django import forms
from .models import Forum


class CreateForumPost(forms.ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"
        exclude = ('user', 'date_time')
