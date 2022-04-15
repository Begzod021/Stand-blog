from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatar/', blank =True, null=True)
    back_avatar = models.ImageField(upload_to='users/avatar/back_avatar', blank=True, null=True)
    telegram = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    date_modefied = models.DateTimeField(auto_now_add=True)
    date_published = models.DateField(auto_now_add=True)




