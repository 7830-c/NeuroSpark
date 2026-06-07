from django.shortcuts import render,reverse
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required #for opening endpoints only when user logged in

@login_required(login_url='/auth/login')
def home(request):
    return render(request,'home.html',{})