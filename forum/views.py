from django.shortcuts import render, HttpResponse
from .models import Forum, Topic, Messages


# Create your views here.
def all_forums(request):
    all_forums = Forum.objects.all()
    context = {
        'forums': all_forums,
    }
    template = 'forum/forum.html'
    return render(request, template, context)

