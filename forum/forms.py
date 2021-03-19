from django import forms
from .models import Forum, Conversation


class CreateNewForum(forms.ModelForm):
    model = Forum
    fields = "__all__"


class CreateNewConversation(forms.ModelForm):
    model = Conversation
    fields = '__all__'
