from django.shortcuts import render

# Create your views here.
def crear_cuenta(request):
    return render(request, 'crear-cuenta.html')

def iniciar_sesion(request):
    return render(request, 'iniciar-sesion.html')