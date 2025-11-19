from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('userLogin/', views.userlogin, name='userlogin'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('bot/', views.bot, name='bot'),
    path("chat/", views.chat_page, name="chat"),
    path("send/", views.send_message, name="send_message"),
    path("fetch/", views.fetch_messages, name="fetch_messages"),
    path('changePassword/', views.changepassword, name='changepassword'),
    path('nearbyHospital/', views.nearbyhospital, name='nearbyhospital'),
    path('logout/', views.logout_view, name='logout'),
]
