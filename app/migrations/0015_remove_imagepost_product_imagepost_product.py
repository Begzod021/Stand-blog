# Generated by Django 4.0.2 on 2022-03-11 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_imagepost_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='product',
        ),
        migrations.AddField(
            model_name='imagepost',
            name='product',
            field=models.ManyToManyField(to='app.Product'),
        ),
    ]