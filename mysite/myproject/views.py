
from multiprocessing import context
from django.views.generic.detail import DetailView
from comments.forms import CommentForm
from comments.models import Comment
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse



def home(request):
    category = Category.objects.all()
    tag1 = Tag.objects.all()
    search_post = request.GET.get('search', '')
    new_post = Post.objects.order_by('id')


    # user_likes = Post.objects.get('likes').count()

    if search_post:
        post = Post.objects.filter(Q(title__icontains=search_post) & Q(text__icontains=search_post)).order_by('-id')
    else:
        post = Post.objects.order_by('-id')
    context = {
        'category':category,
        'post':post,
        'tag1':tag1,
        'new_post':new_post,
        # 'user_likes':user_likes,
    }
    return render(request, 'index.html', context)



def about(request):
    return render(request, 'about.html')


def blog(request):
    category = Category.objects.all()
    tag =Tag.objects.all()
    post = Post.objects.order_by('-id')
    paginator = Paginator(post, 3)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    context = {
        'post':post, 
        'category':category,
        'tag':tag,

        'new_post':post
    }

    return render(request, 'blog.html', context)


def contact(request):
    return render(request, 'contact.html')


def postdetails(request, slug):
    category1 = Category.objects.all()
    tag = Tag.objects.all()

    try:
        post = Post.objects.get(slug=slug)
        post_likes = post.likes.count()
    except:
        post = 0
        post_likes = 0
    post = Post.objects.get(slug=slug)
    image = Photo.objects.filter(post=post)
    category = Category.objects.values_list('id')
    for i in category:
        if Post.objects.filter(category=i[0], slug=slug):
            post_right = Post.objects.filter(category=i[0])

            
    comments = post.comments.filter(parent__isnull=True).order_by('-id')
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
            
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post-details', post.slug)
    else:
        comment_form = CommentForm()



    context = {
        'post':post,
        'post_right':post_right,
        'category':category1,
        'tag':tag,
        'comment_form':comment_form,
        'comments':comments,
        'image':image,
        'post_likes':post_likes,
    }


    return render(request, 'post-details.html', context)

def filter(request, slug):
    category1 = Category.objects.get(slug=slug)
    try:
        post = Post.objects.get(slug=slug)
        post_likes = post.likes.count()
    except:
        post = 0
        post_likes = 0
    post = Post.objects.filter(category=category1).order_by('-id')
    post_category = Post.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)

    context = {
        'post':post,
        'post_category':post_category,
        'category':category,
        'tag':tag,
        'new_post':post,
        'post_likes':post_likes
    }
    return render(request, 'filters/category.html', context)

def filter_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    tag1 = Tag.objects.all()
    post = Post.objects.filter(tag=tag).order_by('-date')
    category = Category.objects.all()
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)
    context = {
        'post':post,
        'category':category,
        'tag':tag1,
        'new_post':post
    }

    return render(request, 'filters/tags.html', context)

def LikeView(request, slug):
    if request.user.is_authenticated:
        post = Post.objects.get(slug=slug)
        post.likes.add(request.user)
        post.save()
    else:
        return redirect('user_login')

    return HttpResponseRedirect(reverse('post-details', args=[str(slug)])) 


def date_post(request, date):
    new_post = Post.objects.filter(date=date).order_by('-id')
    paginator = Paginator(new_post, 3)
    page_number = request.GET.get('page')
    new_post = paginator.get_page(page_number)
    category = Category.objects.all()
    tag = Tag.objects.all()
    context = {
        'new_post':new_post, 
        'category':category,
        'tag':tag
    }

    return render(request, 'date_post/date_post.html', context)
