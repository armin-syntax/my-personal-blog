from django.contrib import admin

from .models import Tag, Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    exclude = ['slug']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'is_published', 'created_at', 'updated_at']
    list_filter = ['is_published', 'created_at', 'updated_at']
    search_fields = ['title', 'slug', 'content']
    exclude = ['slug']
