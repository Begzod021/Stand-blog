from django.db import models
from django.utils.text import slugify
# Create your models here.
from myproject.models import Post
from accounts.models import User


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.author)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    