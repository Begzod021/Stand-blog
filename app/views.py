
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from accounts.models import Worker
from accounts.models import CompanyCategory
from .models import *
from .forms import *
from accounts.models import Company
from comments.models import Comment
from comments.forms import CommentForm
def home(request):
    product = Product.objects.all()
    blog = Blog.objects.all()
    company = Company.objects.all()

    context = {
        'client':blog,
        'company':company,
        'product':product
    }

    return render(request, 'index.html', context)




def about(request):
    return render(request, 'about.html')




def blog(request):
    blog = Blog.objects.all().order_by('-id')
    blog_right = Blog.objects.all().order_by('id')[:3]
    paginator = Paginator(blog, 2)
    page_number = request.GET.get('page')
    blog = paginator.get_page(page_number)
    category = CompanyCategory.objects.all()
    user = Company.objects.all()
    print(user)
    context = {
        'blog':blog,
        'category':category,
        'user':user,
        'new_post':blog,
        'blog_right':blog_right

    }
    return render(request, 'blog.html', context)

def blog_category(request, slug):
    category1 = CompanyCategory.objects.get(slug=slug)
    company1 = Company.objects.filter(category=category1).order_by('-id')
    print(company1)
    blog = Blog.objects.all()
    context = {
        'blog_new':blog,
        'category':category1,
        'company':company1
    }
    return render(request, 'category_blog.html', context)

def blog_single(request, slug):
    blog = Blog.objects.order_by('-id').get(slug=slug)
    category1 = CompanyCategory.objects.all()
    blog_right = Blog.objects.all().order_by('-id')[:4]
    comments = blog.comments.filter(parent__isnull=True).order_by('-id')
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None

            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj
            try:
                new_comment = comment_form.save(commit=False)
                new_comment.post = blog
                new_comment.author = request.user
                new_comment.save()
                return redirect('blogsingle', blog.slug)
            except:
                return redirect('company_register')
    else:
        comment_form = CommentForm()



    context = {
        'blog':blog,
        'category':category1,
        'comment_form':comment_form,
        'comments':comments,
        'blog_right':blog_right

    }
    return render(request, 'blog-single.html', context)



def contact(request):
    return render(request, 'contact.html')







def product(request):
    post = Product.objects.all()
    category = ProductCategory.objects.all()
    context = {
        'post':post,
        'category':category,
    }
    return render(request, 'portfolio.html', context)



def product_category(request, slug):
    category = ProductCategory.objects.get(slug=slug)
    post = Product.objects.filter(category=category)
    category_new = ProductCategory.objects.all()
    context = {
        'post':post,
        'category':category,
        'category_new':category_new
    }
    return render(request, 'product-category.html', context)








def product_single(request, slug):
    post = Product.objects.get(slug=slug)
    image_post = ImagePost.objects.filter(product=post)
    context = {
        'post':post,
        'image':image_post
    }

    return render(request, 'portfolio-details.html', context)












def services(request):
    return render(request, 'services.html')
















def team(request, slug):
    return render(request, 'team.html')






def worker_blog(request, slug):
    form = BlogForm()
    worker_company = Company.objects.get(slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = worker_company
            obj.save()
            form.save()
            return redirect('worker_blog', worker_company.slug)
    context = {
        'form':form,
        'worker_company':worker_company,
    }
    return render(request, 'blog_form.html', context)





def worker_post(request, slug):
    form = ProductForm()
    worker_company = Company.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = worker_company
            obj.save()
            form.save()
            return redirect('worker_post', worker_company.slug)
    
    context = {
        'form':form
    }

    return render(request, 'post_form.html', context)

def worker_image(request,slug):
    form = ImagePostForm()
    worker_company = Company.objects.get(slug=slug)
    product = Product.objects.filter(company=worker_company)
    form = ImagePostForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = worker_company
            obj.save()
            return redirect('worker_image', worker_company.slug)
    context = {
        'form':form,
        'product':product,
    }
    return render(request, 'worker-image.html', context)




def blog_date(request,date):
    blog = Blog.objects.filter(date=date).order_by('-id')
    category = CompanyCategory.objects.all()
    paginator = Paginator(blog, 3)
    page_number = request.GET.get('page')
    blog = paginator.get_page(page_number)

    context = {
        'blog':blog,
        'category':category
    }

    return render(request, 'date_blog.html', context)


def price(request):
    product_price = Product.objects.all()
    context = {
        'product_price':product_price
    }
    return render(request, 'pricing.html', context)
