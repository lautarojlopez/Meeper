from django.shortcuts import redirect, render
from Usuarios.models import Perfil
from .forms import FormEditarPerfil, FormEditarUsuario, UserRegisterForm
from django.contrib.auth.models import User
from Posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def crear_cuenta(request):
    if request.method == "GET":
        return render(request, 'crear-cuenta.html')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            perfil = Perfil(user=user)
            perfil.save()
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