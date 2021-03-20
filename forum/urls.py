from django.urls import path
from . import views

urlpatterns = [
    path('all_forums', views.all_forums, name='all_forums'),
    path('forum_detail/<forum_id>', views.forum_detail, name='forum_detail'),
    path('forum_detail/<forum_id>/new', views.new_topic, name='new_topic'),
]