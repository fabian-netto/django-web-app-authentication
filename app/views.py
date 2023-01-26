from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.models import *
# Create your views here.

@login_required(login_url='login')
def home(request):
    a = Customer.objects.all()
    return render(request,"home.html")

def login(request):
    if request.method == 'POST':
        name = request.POST['uname']
        psw = request.POST['psw']
        b = Customer.objects.filter(uname=name)
        for user in b:
            if user.uname == name and user.psw == psw:
                return redirect(home)
            else:
                return redirect(login)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        psw = request.POST['psw']
        c = Customer.objects.create(uname=uname, email=email, psw=psw)
        c.save()
        return redirect(login)
    return render(request, 'register.html')

