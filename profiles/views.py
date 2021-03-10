from django.shortcuts import render


def profile(request):
    """ Display user profile """
    template = 'profile/profile.html'
    context = {

    }
    return render(request, render, template)
