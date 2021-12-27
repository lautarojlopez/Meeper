# Generated by Django 4.0 on 2021-12-26 02:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Usuarios', '0009_notificacionlike_notificacionfollow_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones_sent', to='auth.user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to='auth.user')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.RemoveField(
            model_name='notificacionfollow',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='notificacionfollow',
            name='to_user',
        ),
        migrations.RemoveField(
            model_name='notificacionlike',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='notificacionlike',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='NotificacionComentario',
        ),
        migrations.DeleteModel(
            name='NotificacionFollow',
        ),
        migrations.DeleteModel(
            name='NotificacionLike',
        ),
    ]