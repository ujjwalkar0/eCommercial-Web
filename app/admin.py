from django.contrib import admin
from .models import Post, Catagories, Profile
# Register your models here.

admin.site.register(Post)
admin.site.register(Catagories)
admin.site.register(Profile)