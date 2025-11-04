from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request,'Html/home.html')

def adminLogin(request):
    return render(request,'Html/adminLogin.html')
