from itertools import product
from turtle import ondrag
from unicodedata import category
from django.conf import settings
from django.utils.text import slugify
from django.db import models
from accounts.models import Company
from accounts.models import CompanyCategory
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250, blank=True)
    text = models.TextField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, related_name='companies')
    image = models.ImageField(upload_to = 'blog/', blank=True)
    video = models.FileField(upload_to='video/', blank=True)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(db_index=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE, related_name='blogs',blank=True, null=True)

    

    def save(self, *args, **kwargs):

        self.slug = slugify(self.title)


        return super().save(*args, **kwargs)



    def __str__(self) -> str:
        return self.title

    def get_comment_count(self):
        return self.comments.count()


class ProductCategory(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True, db_index=True)


    def __str__(self) -> str:
        return self.name


    def save(self, *args, **kwargs):

        slug = f'{self.name}'

        self.slug = slugify(slug)


        return super().save(*args, **kwargs)




class Product(models.Model):

    blog_product = (
        ('',''),
        ('month', 'month'),
    )


    title = models.CharField(max_length=250, blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='post/')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, db_index=True)
    date = models.DateField(auto_now_add=True)
    price = models.CharField(max_length=25, blank=True)
    price_month = models.CharField(max_length=25, default=False, choices=blog_product, blank=True)
    phone = models.PositiveIntegerField(blank=True, null=True)


    def save(self, *args, **kwargs):

        slug = f'{self.category}-{self.title}'

        self.slug = slugify(slug)


        return super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title

class ImagePost(models.Model):
    image = models.ImageField(upload_to='post/single-post/', blank=True)
    product = models.ForeignKey(Product,related_name='posts', on_delete=models.CASCADE)
    company = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)