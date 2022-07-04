from django.contrib import admin

from .models import Forum
from .models import Otvet
from .models import Category

admin.site.register(Forum)
admin.site.register(Otvet)
admin.site.register(Category)