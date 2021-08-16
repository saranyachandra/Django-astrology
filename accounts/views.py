from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.add_message(request,messages.INFO,'username or password incorrect')
            return redirect("login")
    else:
        return render(request,"login.html")

def register(request):

    if request.method == 'POST':
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        username       = request.POST['user']
        pass1       = request.POST['password1']
        pass2       = request.POST['password2']
        email       = request.POST['email']
        
        if pass1 == pass2: 
            if User.objects.filter(username=username).exists():
                messages.add_message(request,messages.INFO,'User already exists')   
                return redirect('register') 
            elif User.objects.filter(email=email).exists() :
                messages.add_message(request,messages.INFO,'email already exists')
                return redirect('register') 
            else:    
                user = User.objects.create_user(username=username,password=pass1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.add_message(request,messages.INFO,'user created')
                return redirect('login') 
        else:
            messages.add_message(request,messages.INFO,'password not match')
            return redirect('register') 
    else:    
        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")