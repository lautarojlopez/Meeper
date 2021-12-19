from django.shortcuts import redirect, render

from Usuarios.models import Perfil
from .forms import UserRegisterForm

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