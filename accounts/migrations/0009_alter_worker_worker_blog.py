# Generated by Django 4.0.2 on 2022-03-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_worker_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='worker_blog',
            field=models.CharField(choices=[('', ''), ('blog', 'blog'), ('post', 'post'), ('post-image', 'post-image')], default=False, max_length=25),
        ),
    ]
