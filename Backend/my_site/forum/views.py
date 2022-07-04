from django.shortcuts import render
from django.http import HttpResponse

from .models import Forum
from .models import Otvet


def index(request):
    forumdate=Forum.objects.order_by('-creattime')
    otvetdate = Otvet.objects.order_by('-creattime')
    context= {
        'forum':forumdate, 
        'otvet':otvetdate
     }
    return render(request, 'forum/index.html',context)

def test(request):
    return HttpResponse('<h1> test 1')