# Generated by Django 4.0 on 2021-12-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=280),
        ),
    ]
