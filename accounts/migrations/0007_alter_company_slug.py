# Generated by Django 4.0.2 on 2022-03-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_worker_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(),
        ),
    ]
