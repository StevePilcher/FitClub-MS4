from django.urls import path
from . import views

urlpatterns = [
    path('forum/', views.forum, name='forum')
    path('addForum/',views.addForum,name='addForum'),
    path('addConversation/',views.addConversation,name='addConversation'),
]