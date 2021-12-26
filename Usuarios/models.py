from django.db import models
from django.contrib.auth.models import User
from Posts.models import *
from itertools import chain

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, default='', null=True)
    img = models.ImageField(default='default.png')

    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'
    
    def siguiendo(self):
        user_ids = Relacion.objects.filter(from_user=self.user).values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    
    def seguidores(self):
        user_ids = Relacion.objects.filter(to_user=self.user).values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)

    def likes(self):
        posts_ids = Like.objects.filter(user=self.user).values_list('post_id', flat=True)
        return Post.objects.filter(id__in=posts_ids)
    
    def notificaciones(self):
        return Notificacion.objects.get(to_user=self.user)
    
    def notificaciones_no_leidas(self):
        notif = Notificacion.objects.filter(to_user=self.user, leida=False)
        return notif

    class Meta:
        verbose_name_plural = 'Perfiles'

class Relacion(models.Model):
    from_user = models.ForeignKey(User, related_name='relaciones', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Relaciones'

    def __str__(self) -> str:
        return f'{self.from_user} sigue a {self.to_user}'

class Notificacion(models.Model):
    to_user = models.ForeignKey(User, related_name='notificaciones', on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, related_name='notificaciones_from', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=15)
    post = models.ForeignKey(Post, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    comentario = models.ForeignKey(Comentario, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    like = models.ForeignKey(Like, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    leida = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Notificaciones"
        ordering = ['-timestamp']
    
    def __str__(self) -> str:
        return f'Notificacion de {self.from_user} para {self.to_user} - {self.tipo}'