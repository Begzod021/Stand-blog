from multiprocessing import context
from pydoc import render_doc
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def company_register(request):
    form = CompanyForm()
    if request.method=='POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.set_password(company.password)
            company.save()
            return redirect('login_company') 
        else:
            return redirect('company_register')

    context = {
        'form':form
    }

    return render(request, 'accounts/register.html', context)

def worker_register(request,slug):
    form = WorkerUserForm()
    company = Company.objects.all().get(slug=slug)
    if request.method == 'POST':
        form = WorkerUserForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user
            obj.save()
            return redirect('account_edit', company.slug)
        else:
            return redirect('worker_register',company.slug)


    context = {
        'form':form,
        'company':company
    }
    return render(request, 'accounts/worker-register.html', context)

def login_company(request):
    form = CompanyForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('company_register')
    
    context = {
        'form':form
    }

    return render(request, 'accounts/login.html', context)

def logout_company(request):
    logout(request)
    return redirect('home')





def worker_login(request, slug):
    form = WorkerUserForm()
    company = Company.objects.all().get(slug=slug)
    worker = Worker.objects.all().filter(slug=company)
    # model = Worker.objects.filter(worker_blog=blog)
    if request.method=='POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = Worker.objects.get(username=username)
        if username==username and password1==password2:
            if company == user.company:
                if user.worker_blog == 'blog':
                    return redirect('worker_blog', company.slug)
                elif user.worker_blog == 'post':
                    return redirect('worker_post',company.slug)
                elif user.worker_blog == 'post-image':
                    return redirect('worker_image', company.slug)
                else:
                    return redirect('worker_login', company.slug)
            else:
                return HttpResponse('You don\'t have an account on this Company')

        else:
            return redirect('worker_register', company.slug)

    context = {
        'form':form,
        'company':company,
        'worker':worker

    }
    return render(request, 'accounts/worker_login.html', context)



def user_profiles(request, slug):
    try:
        userprofiles = Company.objects.all().get(slug=slug)
    except:
        return HttpResponse('Page Not Found')
    
    worker_list = Worker.objects.all()
    print(worker_list)

    context = {
        'userprofile':userprofiles,
        'worker_list':worker_list
    }
    return render(request, 'accounts/profile.html', context)

def company_edit(request, slug):
    company = Company.objects.get(slug=slug)
    company_form = CompanyEdit(request.POST or None, request.FILES or None, instance=company)
    if request.method == 'POST':
        company_form = CompanyEdit(request.POST, request.FILES, instance=company)
        if company_form.is_valid():
            company_form.save()
            return redirect('account_edit', company.slug)

    context = {
        'user':company,
        'form':company_form
    }

    return render(request, 'accounts/editor_user.html', context)
    