from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email= request.POST['email']
        Password = request.POST['Password']
        conform_password = request.POST['conform_password']
        if Password == conform_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
               user = User.objects.create_user(username=username, password=Password, first_name=first_name,
                                            last_name=last_name, email=email)
               user.save()
               return redirect('login')
              # print("User Created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")
