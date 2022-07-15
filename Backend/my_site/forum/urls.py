from django.urls import path
from rest_framework import routers
from .api import *
from .views import ForumView, ComentView, PostView, CitysView
from .views import CoordView

from .views import *

router = routers.DefaultRouter()
router.register('api/post',PostViewSet, 'post')
router.register('api/coment',ComentViewSet, 'coment')
router.register('api/citys',CitysViewSet, 'citys')
router.register('api/profile',ProfileViewSet, 'profile')

urlpatterns = router.urls

app_name = 'profile'
app_name = 'coord'
urlpatterns= [
    path('',index),
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
    path('map/', map, name='map'),
    path('profile/', ForumView.as_view()),
    path('coord/', CoordView.as_view()),
    path('coment/', ComentView.as_view()),
    path('post/', PostView.as_view()),
    path('citys/', CitysView.as_view()),
]
