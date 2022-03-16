from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'company', 'date']
    prepopulated_fields = {'slug':('title',)}
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'company', 'date']
@admin.register(ImagePost)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image']