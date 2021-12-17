from django.shortcuts import render
from Posts.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', { 'posts': posts})