from django.contrib import admin
from .models import Post, Book , Comment, Knowledge


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('created',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ('updated', 'created')



@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'slug')
    list_filter = ('created',)
    search_fields = ('book_title', 'body', 'author')
    prepopulated_fields = {'slug': ('book_title',)}
    date_hierarchy = 'created'
    ordering = ('updated', 'created')


@admin.register(Knowledge)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'slug')
    list_filter = ('created',)
    search_fields = ('tags', 'description', 'author')
    prepopulated_fields = {'slug': ('author',)}
    date_hierarchy = 'created'
    ordering = ('updated', 'created')