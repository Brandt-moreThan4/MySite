from django.contrib import admin
from .models import Post


@admin.register(Post)
class BlogExternalAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'name')
    list_filter = ('date',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    ordering = ('date',)

