from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.db import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = '__all__'

class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Coment
        fields = '__all__'

class CitysSerializer(serializers.ModelSerializer):
    class Meta:
        model= Citys
        fields = '__all__'

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields = '__all__'

class CoordinatSerializer(serializers.ModelSerializer):
    class Meta:
        model= Coordinat
        fields = '__all__'