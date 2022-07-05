from django.contrib import admin

from .models import Post
from .models import Coment
from .models import Category
from .models import Profile

admin.site.register(Post)
admin.site.register(Coment)
admin.site.register(Category)
admin.site.register(Profile)