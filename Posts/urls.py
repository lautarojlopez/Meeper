from django.urls import path
from .views import *

urlpatterns = [
    path('nuevo/', nuevo_post, name="nuevo-post"),
    path('eliminar/<int:id>', eliminar_post, name="eliminar-post"),
    path('<int:post_id>/comentar/', comentar, name="comentar"),
    path('comentario/<int:comentario_id>/eliminar/', eliminar_comentario, name="eliminar-comentario"),
    path('<int:post_id>/like/', like, name='like'),
    path('<int:post_id>/dislike/', dislike, name='dislike'),
]