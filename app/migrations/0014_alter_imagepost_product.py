# Generated by Django 4.0.2 on 2022-03-11 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_imagepost_product_imagepost_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product'),
        ),
    ]
