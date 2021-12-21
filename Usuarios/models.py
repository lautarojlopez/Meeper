from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, default='', null=True)
    img = models.ImageField(default='default.png')

    def __str__(self) -> str:
        return f'Perfil de {self.user.username}'

    class Meta:
        verbose_name_plural = 'Perfiles'
