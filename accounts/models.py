from distutils.command.upload import upload
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import AbstractUser
class CompanyCategory(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True, db_index=True)

    def save(self, *args, **kwargs):

        slug = f'{self.name}'

        self.slug = slugify(slug)


        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

        
    def get_post_count(self):
        return self.blogs.count()




class Company(AbstractUser):






    is_comapny = models.BooleanField(default=False, blank=True)
    is_worker = models.BooleanField(default=False, blank=True)

    logo_company = models.ImageField(upload_to='logo_company/', blank=True)
    bio = models.TextField(blank=True)
    logo = models.ImageField(upload_to = 'logo/', blank=True)
    telegram = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    date_modefied = models.DateTimeField(auto_now_add=True)
    date_published = models.DateField(auto_now_add=True)
    companyname = models.CharField(max_length=250, blank=True)
    companyfile = models.FileField(upload_to='files/', blank=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE, blank=True, null=True, related_name='category')
    companybuildtime = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(db_index=True)
        

    def save(self, *args, **kwargs):

        self.slug = slugify(self.companyname)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.companyname


class Worker(models.Model):
    blog_product = (
        ('',''),
        ('blog', 'blog'),
        ('post', 'post'),
        ('post-image', 'post-image'),
    )
    

    worker_blog = models.CharField(max_length=25, choices=blog_product, default=False)
    is_worker = models.BooleanField(default=False, blank=True)
    is_comapny = models.BooleanField(default=False, blank=True)



    username = models.CharField(max_length=250, blank=True)
    password1 = models.CharField(max_length=250, blank=True)
    password2 = models.CharField(max_length=250, blank=True)
    email = models.EmailField(max_length=250 ,blank=True)
    slug = models.SlugField(db_index=True)
    image = models.ImageField(upload_to ='worker/', blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.company)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.company)

