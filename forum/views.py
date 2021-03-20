from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Forum, Topic, Posts

# Create your views here.
def all_forums(request):
    forums = Forum.objects.all()
    context = {
        'forums': forums,
    }
    template = 'forum/forum.html'
    return render(request, template, context)


def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)

    context = {
        'forum': forum,

    }
    template = 'forum/forum_detail.html'
    return render(request, template, context)


def new_topic(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = get_object_or_404(User, username=request.user)

        topic = Topic.objects.create(
            subject=subject,
            forum=forum,
            originator=user,
        )

        post = Posts.objects.create(
            message=message,
            topic=topic,
            created_by=user,
        )
        messages.success(request, f'Your {topic.subject} has been created')
        return redirect('forum_detail', forum_id=forum.id)

    context = {
        'forum': forum,
    }
    template = 'forum/new_topic.html'

    return render(request, template, context)
