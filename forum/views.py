from django.shortcuts import render, redirect, get_object_or_404
from .models import Forum
from .forms import CreateForumPost
from profiles.models import UserProfile


# Create your views here.

def forum(request):
    """ A view to return the forum"""
    posts = Forum.objects.all()
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'forum/forum.html'
    form = CreateForumPost(instance=profile)
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, template, context)


def add_post(request):
    """A view to add a new forum"""
    profile = get_object_or_404(UserProfile, user=request.user)
    form = CreateForumPost()
    if request.method == 'POST':
        form = CreateForumPost(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('forum')
    context = {'form': form}
    template = 'forum/forum.html'
    return render(request, template, context)
