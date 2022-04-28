from django.urls import path, include
from .views import PostListView, About, Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('posts/', PostListView.as_view(), name='posts'),
]