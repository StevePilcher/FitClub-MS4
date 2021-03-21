from django.urls import path
from . import views

urlpatterns = [
    path('forums', views.all_forums, name='all_forums'),
    path('forums/<forum_id>/', views.forum_detail, name='forum_detail'),
    path('forums/<forum_id>/new', views.new_topic, name='new_topic'),
    path('forums/<forum_id>/topics/<topic_id>', views.topic_posts, name='topic_posts'),
]

