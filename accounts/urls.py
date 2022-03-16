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
    path('register/', company_register, name='company_register'),
    path('<slug:slug>/worker-register/', worker_register, name='worker_register'),
    path('login/', login_company, name='login_company'),
    path('logout/', logout_company, name='logout'),
    path('<slug:slug>/worker-login/', worker_login, name='worker_login'),
    path('profile-company/<slug:slug>/',user_profiles, name='account_edit'),
    path('edit-profile/<slug:slug>/', company_edit, name='company_edit')
]
