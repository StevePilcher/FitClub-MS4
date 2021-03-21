from django import forms
from .models import Posts, Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(max_length=500)

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class NewPostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['message', ]
