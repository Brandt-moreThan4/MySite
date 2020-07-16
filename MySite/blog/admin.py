from django.contrib import admin
from .models import Post #, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('created',)
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ('updated', 'created')



#@admin.register(Comment)
#class PostAdmin(admin.ModelAdmin):
#    list_display = ('name', 'email', 'post', 'created', 'active')
#    list_filter = ('active', 'created', 'updated')
#    search_fields = ('name', 'email', 'body')