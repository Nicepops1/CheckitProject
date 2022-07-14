from django.urls import path
from rest_framework import routers
from .api import *
from .views import ForumView

from .views import *

router = routers.DefaultRouter()
router.register('api/post',PostViewSet, 'post')
router.register('api/coment',ComentViewSet, 'coment')
router.register('api/citys',CitysViewSet, 'citys')
router.register('api/profile',ProfileViewSet, 'profile')

urlpatterns = router.urls

app_name = 'profile'
urlpatterns= [
    path('',index),
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
    path('map/', map, name='map'),
    path('profile/', ForumView.as_view()),
]
