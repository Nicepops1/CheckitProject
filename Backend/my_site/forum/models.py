from django.db import models
from django.conf import settings

class Post(models.Model):
    avtorID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    creattime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    city = models.ForeignKey('Citys', on_delete=models.PROTECT, null=True)
    event = models.BooleanField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    like= models.IntegerField(default=0)
    unlike= models.IntegerField(default=0)
    publik = models.BooleanField(blank=True, default=False)

    def __str__ (self):
        return self.title
   
    class Meta:
        verbose_name = 'Post'
        

class Coment(models.Model):
    avtorID=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)
    postID= models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    creattime = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='userphoto/%Y/%m/%d/', blank=True, null=True)

    def __str__ (self):
        return self.content

class Citys(models.Model):
    city = models.CharField(max_length=150, db_index=True)
    

    def __str__ (self):
        return self.city





class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)