from django.db import models
from django.utils import timezone
from Usuarios.models import User

# Create your models here.
class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self) -> str:
        return f'{self.user.username}: {self.content}'

class Comentario(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=280)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
    
    def __str__(self) -> str:
        return f'Comentario de {self.autor} a {self.post.user}: {self.content}'