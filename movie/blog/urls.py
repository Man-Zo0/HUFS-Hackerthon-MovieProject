from django.contrib import admin
from django.urls import path
from blog.views import *

app_name='blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>', detail, name='detail'),
    path('create_comment/', create_comment, name='create_comment')
]