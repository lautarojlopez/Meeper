from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('iniciar-sesion/', auth_views.LoginView.as_view(template_name="iniciar-sesion.html",redirect_authenticated_user=True), name="iniciar-sesion"),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name="cerrar-sesion"),
    path('crear-cuenta/', crear_cuenta, name="crear-cuenta")
]