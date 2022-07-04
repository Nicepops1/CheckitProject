from django.db import models

class Forum(models.Model):
    avtorID = models.IntegerField()
    title = models.CharField(max_length=150)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    creattime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__ (self):
        return self.title
   
    class Meta:
        verbose_name = 'mes'
        

class Otvet(models.Model):
    avtorID=models.IntegerField()
    postID= models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.TextField()
    creattime = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.content

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def __str__ (self):
        return self.title
