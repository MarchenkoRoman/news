from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_image']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_filter = ['is_published', 'category']
    search_fields = ['title', 'content']
    fields = ['title', 'category', 'content', 'image', 'get_image', 'is_published', 'views']
    readonly_fields = ['get_image', 'views']
    save_on_top = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return 'нет картинки'

    get_image.short_description = 'Картинка'


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']


admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
