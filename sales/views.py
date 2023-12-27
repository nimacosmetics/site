from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'register.html',{'error':'Sorry Username Taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('index')
    return render(request,'register.html')

# def login(request):
#     if request.method=="POST":
#         user = auth.authenticate(username = request.POST['username'], 
#         password = request.POST['password'])
#         if user is not None:
#             auth.login(request,user)
#             return redirect('index')
#         else:
#             return render(request,'login.html',{'error':'Username or Password is incorrect'})
#     else:
#         return render(request,'login.html')
#     return render(request,"login.html")

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('index')
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html", {
        "message": "Logged out."
    })

def products(request):
    return render(request, 'products.html')
def single(request):
    return render(request, 'single-product.html')
