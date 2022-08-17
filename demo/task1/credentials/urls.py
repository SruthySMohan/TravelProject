from django.urls import path,include

from django.urls import path
from . import views
from django.contrib import messages


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]