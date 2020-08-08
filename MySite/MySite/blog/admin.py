from django.contrib import admin
from .models import Knowledge, BlogPost, Book , Comment


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'slug')
    list_filter = ('created',)
    search_fields = ('post_title', 'post_body')
    prepopulated_fields = {'slug': ('post_title',)}
    date_hierarchy = 'created'
    ordering = ('updated', 'created')



@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(Book)
class PostAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'author')
    list_filter = ('created',)
    search_fields = ('book_title', 'post_body', 'author')
    prepopulated_fields = {'slug': ('book_title',)}
    date_hierarchy = 'updated'
    ordering = ('updated', 'created')


@admin.register(Knowledge)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'description')
    list_filter = ('created',)
    search_fields = ('tags', 'description', 'author')
    prepopulated_fields = {'slug': ('author',)}
    date_hierarchy = 'updated'
    ordering = ('updated', 'created')