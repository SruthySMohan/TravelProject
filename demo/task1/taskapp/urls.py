from django.urls import path,include

from taskapp import views


urlpatterns = [
    path('',views.home,name='home'),


   # path('index/',views.index,name="index"),
   # path('add/',views.addition,name='addition'),
    #path('contact/',views.contact,name='contact'),
   # path('logout/',views.logout,name='logout')

]
