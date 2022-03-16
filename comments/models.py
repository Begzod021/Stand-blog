

# Create your models here.
from django.db import models
from app.models import Blog
from accounts.models import Company
from ckeditor.fields import RichTextField
class Comment(models.Model):
    text = RichTextField()
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)

    def __str__(self) -> str:
        return str(self.author)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'