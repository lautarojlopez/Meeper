from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from Usuarios.models import Notificacion, Perfil, Relacion
from .forms import FormEditarPerfil, FormEditarUsuario, UserRegisterForm
from django.contrib.auth.models import User
from Posts.models import Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
def crear_cuenta(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "GET":
        return render(request, 'crear-cuenta.html')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            perfil = Perfil(user=user)
            perfil.save()
            messages.success(request, 'Tu cuenta ha sido creada')
            return redirect('home')
        else:
            return render(request, 'crear-cuenta.html', { 'errors': form.errors })

def iniciar_sesion(request):
    return render(request, 'iniciar-sesion.html')

# Ver Perfil
def ver_perfil(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    return render(request, 'ver-perfil.html', { 'user': user, 'posts':posts })

# Editar perfil
@login_required
def editar_perfil(request):
    if request.method == "GET":
        form_user = FormEditarUsuario(instance=request.user)
        form_perfil = FormEditarPerfil(instance=request.user.perfil)
        return render(request, 'editar-perfil.html', { 'form_user': form_user, 'form_perfil':form_perfil })
    if request.method == "POST":
        form_user = FormEditarUsuario(request.POST, instance=request.user)
        form_perfil = FormEditarPerfil(request.POST, request.FILES, instance=request.user.perfil)
        if form_user.is_valid() and form_perfil.is_valid():
            try:
                form_user.save()
                form_perfil.save()
                return redirect('ver-perfil', username=request.user.username)
            except Exception as e:
                print(e)

@login_required
@csrf_exempt
def follow(request, username):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        try:
            user = User.objects.get(username=username)
            follow = Relacion(from_user=request.user, to_user=user)
            follow.save()
            notificacion = Notificacion(from_user=request.user, to_user=user, tipo="follow")
            notificacion.save()
            return HttpResponse(200)
        except:
            return HttpResponse(500)

@login_required
@csrf_exempt
def unfollow(request, username):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        try:
            user = User.objects.get(username=username)
            follow = Relacion.objects.get(from_user=request.user, to_user=user)
            follow.delete()
            notificacion = Notificacion.objects.get(from_user=request.user, to_user=user, tipo="follow")
            notificacion.delete()
            return HttpResponse(200)
        except:
            return HttpResponse(500)

@login_required
def ver_notificaciones(request):
    notificaciones = Notificacion.objects.filter(to_user=request.user)
    return render(request, 'notificaciones.html', { 'notificaciones': notificaciones })

@csrf_exempt
@login_required
def leer_notificaciones(request):
    if request.method == "GET":
        return redirect(request.META.get('HTTP_REFERER'))
    if request.method == "POST":
        no_leidas = Notificacion.objects.filter(to_user=request.user, leida=False)
        for noti in no_leidas:
            noti.leida = True
            noti.save()
        return HttpResponse(200)