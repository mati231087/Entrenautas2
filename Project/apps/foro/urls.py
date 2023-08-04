from django.urls import path
from django.views.generic import ListView
from django.db.models import Prefetch
from .models import Post, Comment
from .views import home
from django.shortcuts import render


app_name = 'usuario'

urlpatterns = [
    path('', home, name='home'),
]

def home(request):
    posts = Post.objects.select_related('author').all()
    prefetch = Prefetch('comments', queryset=Comment.objects.select_related('author'))
    posts = posts.prefetch_related(prefetch)
    return render(request, 'foro/home.html', {'posts': posts})
