from django.shortcuts import render
from django.http import HttpResponse
def adminLogin(request):
    return render(request,'Html/adminLogin.html')