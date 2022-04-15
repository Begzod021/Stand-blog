from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'author']
    prepopulated_fields = {'slug':('title',)}
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['image', 'id']
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']