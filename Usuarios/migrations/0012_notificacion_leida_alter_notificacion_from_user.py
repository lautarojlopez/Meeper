# Generated by Django 4.0 on 2021-12-26 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Usuarios', '0011_alter_notificacion_options_notificacion_comentario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='leida',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notificacion',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_from', to='auth.user'),
        ),
    ]
