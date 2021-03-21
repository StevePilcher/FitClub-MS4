from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Forum, Topic, Posts
from profiles.models import UserProfile


@login_required
def all_forums(request):
    """Start view from Nav link to show all forums in the DB"""
    forums = Forum.objects.all()
    context = {
        'forums': forums,
    }
    template = 'forum/forum.html'
    return render(request, template, context)


@login_required
def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)

    context = {
        'forum': forum,

    }
    template = 'forum/forum_detail.html'
    return render(request, template, context)


@login_required
def new_topic(request, forum_id):
    """create a new topic and redirect to forum details view"""
    forum = get_object_or_404(Forum, pk=forum_id)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = get_object_or_404(UserProfile, user=request.user)

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


def topic_posts(request, forum_id, topic_id):
    """A view to render the individual
    topic and posts within that topic"""

    topic = get_object_or_404(Topic, forum_id=forum_id, pk=topic_id)

    return render(request, 'forum/topic_posts.html', {'topic': topic})


def post_reply(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        user = request.POST['user']
        message = request.POST['reply']

        post = Posts.objects.create(
            message=message,
            topic=topic,
            created_by=user,
        )

        messages.success(request, f'Your reply to {topic.subject} has been posted')
        return render(request, 'forum/topic_posts.html', {'topic': topic})

    template = 'forum/new_reply.html'

    return render(request, template)
