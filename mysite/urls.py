
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('another', views.another, name='another'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login')

]
