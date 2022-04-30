
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import *

class Home(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'