# Generated by Django 4.0 on 2021-12-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0012_notificacion_leida_alter_notificacion_from_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
