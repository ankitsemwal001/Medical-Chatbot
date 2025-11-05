from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request,'Html/home.html')

def adminLogin(request):
    return render(request,'Html/adminLogin.html')

def profile(request):
    return render(request,'Html/profile.html')

def bot(request):
    return render(request,'Html/bot.html')

def changePassword(request):
    return render(request,'Html/changePassword.html')

def footer(request):
    return render(request,'Html/footer.html')

def header(request):
    return render(request,'Html/header.html')

def Loginpage(request):
    return render(request,'Html/Loginpage.html')

def logout(request):
    return render(request,'Html/logout.html')

def nearByhospital(request):
    return render(request,'Html/nearByhospital.html')

def UserLogin(request):
    return render(request,'Html/UserLogin.html')
