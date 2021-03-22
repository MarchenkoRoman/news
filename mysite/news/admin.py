from django.contrib import admin
from .models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_filter = ['is_published', 'category']
    search_fields = ['title', 'content']


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
