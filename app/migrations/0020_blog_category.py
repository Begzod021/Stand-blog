# Generated by Django 4.0.2 on 2022-03-12 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_worker_worker_blog'),
        ('app', '0019_alter_blog_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='accounts.companycategory'),
        ),
    ]
