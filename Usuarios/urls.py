from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('iniciar-sesion/', auth_views.LoginView.as_view(template_name="iniciar-sesion.html",redirect_authenticated_user=True), name="iniciar-sesion"),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name="cerrar-sesion"),
    path('crear-cuenta/', crear_cuenta, name="crear-cuenta"),
    path('@<username>', ver_perfil, name="ver-perfil"),
    path('editar-perfil', editar_perfil, name="editar-perfil"),
    path('follow/<username>', follow, name="follow"),
    path('unfollow/<username>', unfollow, name="unfollow"),
    path('notificaciones/', ver_notificaciones, name="notificaciones"),
    path('notificaciones/leer/', leer_notificaciones),
    path('restablecer-contraseña/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('restablecer-contraseña/done', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('restablecer/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('restablecer-contraseña/complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")


]