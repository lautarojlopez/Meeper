# Generated by Django 4.0 on 2021-12-19 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_alter_perfil_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='img',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]