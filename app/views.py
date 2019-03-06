from django.shortcuts import render

# Create your views here.
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'app/index.html'

class SearchView(generic.TemplateView):
    template_name = 'app/search.html'

class DetailView(generic.TemplateView):
    template_name = 'app/detail.html'