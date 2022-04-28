
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Post

class Home(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    template_name = 'all_posts.html'
    model = Post
    context_object_name = 'posts'