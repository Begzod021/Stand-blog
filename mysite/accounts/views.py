
from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse

from myproject.forms import TagForm
from myproject.forms import PhotoForm
from .forms import EditForm, UserForm
from .models import User
from myproject.forms import PostForm,PhotoForm,TagForm
from myproject.models import Post
# Create your views here.
def user_registor(request):
    form = UserForm()
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save( commit=False)
            user.set_password(user.password)
            user.save()
            form.save()
            return redirect('user_login')
        else:
            return redirect('user_register')
    context = {
        'form':form
    }
    return render(request, 'account/register.html', context)

def user_login(request):
    form = UserForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('user_register')
    context = {
        'form':form
    }
    return render(request, 'account/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def user_profiles(request, username):
    try:
        userprofiles = User.objects.all().get(username=username)
    except:
        return HttpResponse('Page Not Found')

    form = PostForm(request.POST, request.FILES)
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            author = User.objects.all().get(username=username)
            obj.author = author
            obj.save()
            form.save()
            return redirect('user_profiles', request.user.username)
    posts = Post.objects.filter(author=userprofiles).order_by('-id')
    form_f = PostForm()
    form_r = TagForm(request.POST)
    if request.method == 'POST':
        form_r = TagForm(request.POST)
        if form_r.is_valid():
            form_r.save()
            return redirect('user_profiles', request.user.username)
    form_i = PhotoForm(request.POST, request.FILES)
    if request.method=='POST':
        form_i = PhotoForm(request.POST, request.FILES)
        if form_i.is_valid():
            form_i.save()
            return redirect('user_profiles', request.user.username)
    context = {
        'userprofile':userprofiles,
        'posts':posts,
        'form_f':form_f,
        'form_r':form_r,
        'form_i':form_i
    }
    return render(request, 'account/profile.html', context)

def user_edit(request, username):
    user = User.objects.get(username=username)
    form = EditForm(request.POST or None, request.FILES or None, instance=user)
    if request.method=='POST':
        form = EditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profiles', request.user.username)
    
    context = {
        'user':user,
        'form':form
    }
    return render(request, 'account/editor_user.html', context)

def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect(user_profiles, request.user.username)

def post_edit(request, slug):
    post = Post.objects.get(slug=slug)

    edit_form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method=='POST':
        edit_form = PostForm(request.POST, request.FILES, instance=post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('user_profiles', request.user.username)
    
    context = {
        'edit_form':edit_form
    }
    return render(request, 'account/post_edit.html', context)

