from django.shortcuts import render
from forum.models import Posts


# Create your views here.


def index(request):
    """A view to return the index page"""
    posts = Posts.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'home/index.html', context)
