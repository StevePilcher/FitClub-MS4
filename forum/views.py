from django.shortcuts import render

# Create your views here.

def forum(request):
    """ A view to return the forum"""
    return render(request, 'forum/forum.html')
