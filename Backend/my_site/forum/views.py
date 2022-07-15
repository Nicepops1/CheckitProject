from django.shortcuts import render, redirect
from django.http import HttpResponse
from .serializers import ProfilSerializer, CoordinatSerializer
from .models import Post
from .models import Profile
from .models import Coment
from .models import Coordinat
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated


class ForumView(APIView):
    permission_classes = IsAuthenticated, )
    def get(self, request):
        profiles = Profile.objects.all()
        serializers = ProfilSerializer(profiles, many=True)
        return Response (serializers.data)
    def post(self, request):
        profile = ProfilSerializer(data=request.data)
        if profile.is_valid():
            profile.save()
        return Response (status=201)

class CoordView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get(self, request):
        coords = Coordinat.objects.all()
        serializers = CoordinatSerializer(coords, many=True)
        return Response (serializers.data)
    def post(self, request):
        coord = CoordinatSerializer(data=request.data)
        if coord.is_valid():
            coord.save()
        return Response (status=201)



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