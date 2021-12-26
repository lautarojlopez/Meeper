# Generated by Django 4.0 on 2021-12-25 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Usuarios', '0007_alter_perfil_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relaciones', to='auth.user')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_to', to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'Relaciones',
            },
        ),
    ]
