from django.contrib import admin
from .models import Movies, Staff, Comment

# Register your models here.
admin.site.register(Movies)
admin.site.register(Staff)
admin.site.register(Comment)