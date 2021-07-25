from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'account'
 
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout' ),
]