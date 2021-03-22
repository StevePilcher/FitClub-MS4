from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Forum, Topic, Posts
from .forms import NewPostsForm, NewTopicForm
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
    topics = forum.topics.order_by('last_updated').annotate(replies=Count('posts'))
    context = {
        'forum': forum,
        'topics': topics,
    }
    template = 'forum/forum_detail.html'
    return render(request, template, context)


@login_required
def new_topic(request, forum_id):
    """create a new topic via Forms and redirect to forum details view"""
    forum = get_object_or_404(Forum, pk=forum_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.originator = user
            topic.forum = forum
            topic.save()
            post = Posts.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user,
            )

            messages.success(request, f'Your {topic.subject} has been created')
            return redirect('forum_detail', forum_id=forum.id)
    else:
        form = NewTopicForm()
        context = {
            'forum': forum,
            'form': form,
        }
        template = 'forum/new_topic.html'
        return render(request, template, context)


@login_required
def topic_posts(request, forum_id, topic_id):
    """A view to render the individual
    topic and posts within that topic"""

    topic = get_object_or_404(Topic, forum_id=forum_id, pk=topic_id)

    return render(request, 'forum/topic_posts.html', {'topic': topic})


@login_required
def post_reply(request, forum_id, topic_id):
    topic = get_object_or_404(Topic, forum_id=forum_id, pk=topic_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = NewPostsForm(request.POST, instance=post_reply)
        if form.is_valid():
            post = form.save()
            print('back to post reply')
            post.topic = topic
            post.created_by = user
            post.save()
            messages.success(request, 'Your reply has been posted')
            return redirect('topic_posts', forum_id=forum_id, topic_id=topic_id)
    else:
        form = NewPostsForm()
    return render(request, 'forum/new_reply.html', {'form': form, 'topic': topic})


@login_required
def edit_posts(request, forum_id, topic_id, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    topic = get_object_or_404(Topic, forum_id=forum_id, pk=topic_id)

    if request.method == 'GET':
        return render(request, 'forum/edit_reply.html', {
            'post': post,
            'topic': topic
        })

    form = NewPostsForm(request.POST, instance=post)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            post.topic = topic
            post.created_by = user
            post.save()
            messages.success(request, 'Your reply has been posted')
            return redirect('topic_posts', forum_id=forum_id, topic_id=topic_id)

    return render(request, 'forum/topic_posts.html', {'topic': topic})