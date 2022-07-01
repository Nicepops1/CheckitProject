from django.db import models

class Forum(models.Model):
    avtorID = models.IntegerField()
    teg = models.TextField()
    title = models.CharField(max_length=150)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    creattime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)

class Otvet(models.Model):
    avtorID=models.IntegerField()
    postID=models.IntegerField()
    content = models.TextField()
    creattime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)