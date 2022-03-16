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



from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('contact', contact, name='contact'),
    path('pricing/', price, name='price'),
    path('services/', services, name='services'),
    path('blog-single/<slug:slug>/', blog_single, name='blogsingle'),
    path('product_singel/<slug:slug>', product_single, name='productsingle'),
    path('team/<slug:slug>', team, name='team'),
    path('<slug:slug>/blog_form/', worker_blog, name='worker_blog'),
    path('<slug:slug>/post_form/', worker_post, name='worker_post'),
    path('product-category/<slug:slug>/', blog_category, name='blog_category'),
    path('blog/<str:date>/', blog_date, name='blog_date'),
    path('<slug:slug>/post_image', worker_image, name='worker_image'),
    path('category/<slug:slug>/', product_category, name='product_category')
]
