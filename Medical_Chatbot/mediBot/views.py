from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import random
from .models import ChatMessage


def home(request):
    return render(request,'Html/home.html')


def profile(request):
    if not request.user.is_authenticated and not request.session.get('is_admin'):
        return redirect('UserLogin')
    return render(request,'Html/profile.html')

def bot(request):
    if not request.user.is_authenticated and not request.session.get('is_admin'):
        return redirect('UserLogin')
    if request.method == 'POST':
        symptoms = request.POST.get('symptoms')
        if 'fever' in symptoms.lower() or 'cough' in symptoms.lower():
            prediction = "Possible flu or cold. Consult a doctor."
        elif 'headache' in symptoms.lower():
            prediction = "Possible migraine or tension headache. Rest and hydrate."
        else:
            prediction = "No disease detected based on symptoms. Stay healthy!"
        return render(request, 'Html/bot.html', {'prediction': prediction, 'symptoms': symptoms})
    return render(request,'Html/bot.html')

def chat_page(request):
    return render(request, "chat.html")


def send_message(request):
    if request.method == "POST":
        user_msg = request.POST.get("message")

        # Save user message
        ChatMessage.objects.create(sender="user", message=user_msg)

        # Simple bot reply (you can replace with AI later)
        replies = [
            "Okay, I understand.",
            "Great!",
            "Tell me more...",
            "Interesting.",
            "Can you explain that?"
        ]
        bot_reply = random.choice(replies)

        # Save bot message
        ChatMessage.objects.create(sender="bot", message=bot_reply)

        return JsonResponse({"reply": bot_reply})

    return JsonResponse({"error": "Invalid request"}, status=400)



def fetch_messages(request):
    messages = ChatMessage.objects.order_by("created_at")
    data = []

    for msg in messages:
        data.append({
            "sender": msg.sender,
            "message": msg.message,
            "time": msg.created_at.strftime("%H:%M")
        })

    return JsonResponse({"messages": data})




def changePassword(request):
    if not request.user.is_authenticated and not request.session.get('is_admin'):
        return redirect('UserLogin')
    return render(request,'Html/changePassword.html')

def footer(request):
    return render(request,'Html/footer.html')

def header(request):
    if request.method == "POST" and request.POST.get("login"):
        return render(request, 'Html/login.html')
    return render(request, 'Html/home.html')


def UserLogin(request):
    return render(request,'Html/UserLogin.html')

def logout(request):
    logout(request)
    request.session.flush()
    return redirect('login')

def nearByhospital(request):
    if not request.user.is_authenticated and not request.session.get('is_admin'):
        return redirect('UserLogin')
    return render(request,'Html/nearByhospital.html')
