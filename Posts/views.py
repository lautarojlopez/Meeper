from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from Usuarios.models import Notificacion
from .models import Comentario, Like, Post
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
            if len(comentario.content) > 280:
                return HttpResponse(500)
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
            if comentario.post.user != request.user:
                try:
                    notificacion = Notificacion(from_user=request.user, to_user=comentario.post.user, tipo="comentario", comentario=comentario, post=comentario.post)
                    notificacion.save()
                except:
                    return HttpResponse(500)
            return HttpResponse(json.dumps(datos))
        except:
            return HttpResponse(500)

@login_required
@csrf_exempt
def eliminar_comentario(request, comentario_id):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "DELETE":
        comentario = Comentario.objects.get(id=comentario_id)
        if comentario.autor == request.user:
            try:
                comentario.delete()
                if comentario.post.user != request.user:
                    try:
                        notificacion = Notificacion.objects.get(from_user=request.user, to_user=comentario.post.user, tipo="comentario", comentario=comentario, post=comentario.post)
                        notificacion.delete()
                    except:
                        return HttpResponse(500)
                return HttpResponse(200)
            except:
                return HttpResponse(500)
        else:
            return HttpResponse(500)

@login_required
@csrf_exempt
def like(request, post_id):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        try:
            post = Post.objects.get(id=post_id)
            like = Like(user=request.user, post=post)
            like.save()
            if post.user != request.user:
                try:
                    notificacion = Notificacion(from_user=request.user, to_user=post.user, tipo="like", like=like)
                    notificacion.save()
                except:
                    return HttpResponse(500)
            return HttpResponse(200)
        except:
            return HttpResponse(500)

@login_required
@csrf_exempt
def dislike(request, post_id):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        try:
            post = Post.objects.get(id=post_id)
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return HttpResponse(200)
        except:
            return HttpResponse(500)

def ver_publicacion(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    print(post)
    if post:
        return render(request, 'ver-publicacion.html', { 'post': post })
    else:
        return HttpResponse('XD')