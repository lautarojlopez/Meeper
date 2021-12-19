from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
from .forms import FormPost

# Create your views here.
def nuevo_post(request):
    if request.method == "GET":
        return redirect('home')
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            post = Post()
            post.content = form.cleaned_data['content']
            post.user = request.user
            post.save()
            return redirect('home')

def eliminar_post(request, id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        try:
            post.delete()
            return HttpResponse("success", status=200)
        except:
            return HttpResponse("error", status=500)
    else:
        return HttpResponse("error", status=500)