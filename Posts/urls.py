from django.urls import path
from .views import *

urlpatterns = [
    path('nuevo/', nuevo_post, name="nuevo-post"),
    path('eliminar/<int:id>', eliminar_post, name="eliminar-post"),
    path('<int:post_id>/comentar/', comentar, name="comentar"),
]