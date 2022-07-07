from .models import *
from rest_framework import viewsets, permissions
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer

class ComentViewSet(viewsets.ModelViewSet):
    queryset = Coment.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer

class CitysViewSet(viewsets.ModelViewSet):
    queryset = Citys.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer