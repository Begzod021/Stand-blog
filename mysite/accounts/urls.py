"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('register', user_registor, name='user_register'),
    path('login', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('profile/<str:username>', user_profiles, name='user_profiles'),
    path('edit/<str:username>', user_edit, name='user_editor'),
    path('delete/<int:pk>/', delete_post, name='delete_post'),
    path('edit_post/<slug:slug>/', post_edit, name='post_edit')
]
