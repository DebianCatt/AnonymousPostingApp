from django.db import models


class Post(models.Model):
    content = models.TextField(max_length=1000)
    owner_id = models.UUIDField(db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'Post #{self.id}'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    content = models.TextField(max_length=500)
    owner_id = models.UUIDField(db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment #{self.id}'