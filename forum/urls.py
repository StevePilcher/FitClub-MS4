from django.urls import path
from . import views

urlpatterns = [
    path('all_forums', views.all_forums, name='all_forums')
]