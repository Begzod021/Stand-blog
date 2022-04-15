from django.db import models
from django.utils.text import slugify
from accounts.models import User




class Category(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    name = models.CharField(max_length=250)
    

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs): 

        slug = f"{self.name}"

        self.slug = slugify(slug)

        return  super().save(*args, **kwargs)


class Tag(models.Model):
    tag = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, db_index=True)
    def __str__(self) -> str:
        return self.tag

    def save(self, *args, **kwargs): 

        slug = f"{self.tag}"

        self.slug = slugify(slug)

        return  super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/images', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
    def __str__(self) -> str:
        return self.title


    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        slug = f'{self.category}-{self.title}'

        self.slug = slugify(slug)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def get_comment_count(self):
        return self.comments.count()



class Photo(models.Model):
    image = models.ImageField(upload_to='post/images')
    post = models.ManyToManyField(Post, related_name='posts')
