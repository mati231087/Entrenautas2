from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image']
    list_filter = ['author']
    search_fields = ['title', 'content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author', 'post']
    list_filter = ['author', 'post']
    search_fields = ['content']

