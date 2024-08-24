from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_time', 'likes_count', 'comments_count', 'shares_count')
    search_fields = ('message',)
    list_filter = ('created_time', 'likes_count')
