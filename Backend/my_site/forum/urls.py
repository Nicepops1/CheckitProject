from django.urls import path
from .views import *
urlpatterns= [
    path('',index),
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
]



