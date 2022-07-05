from django.contrib import admin

from .models import Post
from .models import Coment
from .models import Citys
from .models import Profile

admin.site.register(Post)
admin.site.register(Coment)
admin.site.register(Citys)
admin.site.register(Profile)