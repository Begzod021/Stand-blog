# Generated by Django 4.0.2 on 2022-03-10 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_imagepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='slug',
            field=models.SlugField(default=False),
        ),
    ]