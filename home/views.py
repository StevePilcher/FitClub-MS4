from django.shortcuts import render
from forum.models import Posts


# Create your views here.


def index(request):
    """A view to return the index page and dashboard for logged in user"""
    posts = Posts.objects.all().order_by('-created_at')[:2]
    context = {
        'posts': posts,
    }

    return render(request, 'home/index.html', context)
