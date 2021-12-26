from django.shortcuts import render
from Posts.models import Post
from django.contrib.auth.decorators import login_required
from itertools import chain

from Usuarios.models import Relacion

# Create your views here.
@login_required
def home(request):
    siguiendo = request.user.perfil.siguiendo()
    posts_siguiendo = Post.objects.filter(user__in=siguiendo)
    posts_usuario = Post.objects.filter(user=request.user)
    posts = sorted(chain(posts_siguiendo, posts_usuario), key=lambda data: data.timestamp, reverse=True)
    return render(request, 'index.html', { 'posts': posts})