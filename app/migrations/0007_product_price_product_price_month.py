# Generated by Django 4.0.2 on 2022-03-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_blog_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='product',
            name='price_month',
            field=models.CharField(choices=[('', ''), ('month', 'month')], default=False, max_length=25),
        ),
    ]