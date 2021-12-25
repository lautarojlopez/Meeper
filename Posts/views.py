from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Comentario, Post
from .forms import FormPost
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def nuevo_post(request):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            post = Post()
            post.content = form.cleaned_data['content']
            post.user = request.user
            post.save()
            return redirect(request.META.get('HTTP_REFERER'))

@csrf_exempt
def eliminar_post(request, id):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "DELETE":
        post = Post.objects.get(id=id)
        if post.user == request.user:
            try:
                post.delete()
                return HttpResponse("success", status=200)
            except:
                return HttpResponse("error", status=500)
        else:
            return HttpResponse("error", status=500)

def comentar(request, post_id):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        try:
            comentario = Comentario()
            comentario.content = json.loads(request.body.decode('utf-8'))['content']
            comentario.autor = request.user
            comentario.post = Post.objects.get(id=post_id)
            comentario.save()
            datos = {
                'username': request.user.username,
                'nombre': request.user.first_name,
                'img': request.user.perfil.img.url,
                'content': comentario.content,
                'id': comentario.id,
            }
            return HttpResponse(json.dumps(datos))
        except:
            return HttpResponse(500)

@csrf_exempt
def eliminar_comentario(request, comentario_id):
    if request.method == "GET":
        return redirect('home')
    if request.method == "DELETE":
        comentario = Comentario.objects.get(id=comentario_id)
        if comentario.autor == request.user:
            try:
                comentario.delete()
                return HttpResponse(200)
            except:
                return HttpResponse(500)
        else:
            return HttpResponse(500)