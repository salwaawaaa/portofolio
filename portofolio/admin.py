from django.contrib import admin

# Register your models here.

from .models import post, Tag
admin.site.register(post)
admin.site.register(Tag)