from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib.auth.models import User


from django.contrib.auth import authenticate #for verifying user
from django.contrib.auth import login,logout #for session management
from django.contrib.auth.decorators import login_required #for opening endpoints only when user logged in
 

from django.contrib import messages





def register_page(request):
    if(request.method == "POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        email=request.POST.get('email')

        user=User.objects.filter(username=username)

        if(user.exists()):
            messages.info(request,"Username already taken")
            return redirect(reverse('register_page'))
        
        if(password!=confirm_password):
            messages.info(request,"Passwords do not match")
            return redirect(reverse('register_page'))


        user=User.objects.create(username=username,email=email)
        user.set_password(confirm_password)
        user.save()
        messages.info(request,"Account created successfully")

        return redirect(reverse('register_page'))
        

    return render(request,"registration.html",{})


def login_page(request):
    if(request.method == "POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')

        if(not User.objects.filter(username=username).exists()):
            messages.error(request,"User not exist")
            return redirect(reverse('login_page'))
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Invalid Password")
            return redirect(reverse('login_page'))
        else:
            login(request,user)
            return redirect(reverse('home_page'))
        
    return render(request,"login.html",{})


def logout_page(request):
    logout(request)
    return redirect(reverse('login_page'))


from .utils import *

def reset_password(request):
    send_email_to_client()


