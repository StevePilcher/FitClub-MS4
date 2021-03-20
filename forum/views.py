from django.shortcuts import render, get_object_or_404
from .models import Forum, Topic, Messages


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
