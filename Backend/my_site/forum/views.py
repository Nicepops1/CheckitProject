from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post
from .models import Coment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def index(request):
    forumdate=Post.objects.order_by('-creattime')
    otvetdate = Coment.objects.order_by('-creattime')
    context= {
        'forum':forumdate, 
        'otvet':otvetdate
     }
    return render(request, 'forum/index.html',context)

def test(request):
    return HttpResponse('<h1> test 1')

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register-success')
            return redirect('login')
        else:
            messages.error(request, 'Access denied')
    else:
        form=UserCreationForm()
    return render(request, 'forum/register.html', {"form": form})

def user_login(request):
    return render(request, 'forum/login.html')