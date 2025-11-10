from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request,'Html/home.html')

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'ankit001' and password == '@anki001':
            # Simulate admin login, perhaps set a session or redirect
            request.session['is_admin'] = True
            return redirect('adminhome')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'Html/adminLogin.html')

def profile(request):
    if not request.user.is_authenticated and not request.session.get('is_admin'):
        return redirect('Loginpage')
    return render(request,'Html/profile.html')

def bot(request):
    if not request.user.is_authenticated and not request.session.get('is_admin'):
        return redirect('Loginpage')
    return render(request,'Html/bot.html')

def changePassword(request):
    if not request.user.is_authenticated and not request.session.get('is_admin'):
        return redirect('Loginpage')
    return render(request,'Html/changePassword.html')

def footer(request):
    return render(request,'Html/footer.html')

def header(request):
    return render(request,'Html/header.html')

def Loginpage(request):
    return render(request,'Html/Loginpage.html')

def logout_view(request):
    logout(request)
    request.session.flush()  # Clear session for admin too
    return redirect('home')

def nearByhospital(request):
    if not request.user.is_authenticated and not request.session.get('is_admin'):
        return redirect('Loginpage')
    return render(request,'Html/nearByhospital.html')

def adminhome(request):
    if not request.session.get('is_admin'):
        return redirect('Loginpage')
    return render(request,'Html/adminhome.html')

def viewuser(request):
    if not request.session.get('is_admin'):
        return redirect('Loginpage')
    return render(request,'Html/viewuser.html')

def manageoption(request):
    if not request.session.get('is_admin'):
        return redirect('Loginpage')
    return render(request,'Html/manageoption.html')

def UserLogin(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        elif 'register' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect('home')
    return render(request,'Html/UserLogin.html')
