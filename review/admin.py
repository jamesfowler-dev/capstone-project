from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# Register your models here.
admin.site.register(Comment)


@admin.register(Review)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
