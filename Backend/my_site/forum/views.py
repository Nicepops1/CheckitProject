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
        'Post':forumdate, 
        'Coment':otvetdate
     }
    return render(request, 'forum/index.html',context)
def map(request):
    PostMark=Post.objects.order_by('creattime')
    context1= {
        'Mark':PostMark
     }
    return render(request, 'map/index.html', context1)

def test(request):
    return HttpResponse('<h1> test 1')

def register(request):
    if request.method == 'POST':
        form1=UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Register-success')
            return redirect('login')
        else:
            messages.error(request, 'Access denied')
    else:
        form1=UserCreationForm()
    return render(request, 'forum/register.html', {"form1": form1})

def user_login(request):
    return render(request, 'forum/login.html')