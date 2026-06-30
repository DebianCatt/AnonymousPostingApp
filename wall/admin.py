from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'owner_id',
    )

    search_fields = (
        'content',
    )

    ordering = (
        '-created_at',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'post',
        'created_at',
        'owner_id',
    )

    search_fields = (
        'content',
    )

    ordering = (
        '-created_at',
    )