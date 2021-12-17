from django.urls import path
from .views import *

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name="login"),
    path('crear-cuenta/', crear_cuenta, name="signup")
]