from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
    path('search', views.SearchView.as_view(), name='search'),
    path('detail', views.DetailView.as_view(), name='detail'),
]