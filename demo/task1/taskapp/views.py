from django.shortcuts import render

from .models import Place
from .models import Teamleaders


# Create your views here.
def home(request):
    obj=Place.objects.all()
    obj1=Teamleaders.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})




#def about(request):
 #   return render(request,"about.html")
#def contact(request):
 #   return render(request,"contact.html")
#def logout(request):
 #   return render(request,"logout.html")
#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # addn=x+y
    #subn=x-y
 #   multn=x*y
  #  divn=x/y
   # return render(request,"result.html",{'add':addn,'sub':subn,'mult':multn,'div':divn})
# def register(request):
#     return render(request,"register.html")


# def login(request):
#     return render(request,"login.html")
