from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Component


@admin.register(Component)
class ComponentAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('name', 'price', 'category')
    search_fields = ['name', 'description']
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)
