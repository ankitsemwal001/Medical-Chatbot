from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminLogin/', views.adminlogin, name='adminlogin'),
    path('userLogin/', views.userlogin, name='userlogin'),
    path('register/', views.register, name='register'),
    path('adminhome/', views.admin_home, name='adminhome'),
    path('profile/', views.profile, name='profile'),
    path('bot/', views.bot, name='bot'),
    path('changePassword/', views.changepassword, name='changepassword'),
    path('nearbyHospital/', views.nearbyhospital, name='nearbyhospital'),
    path('logout/', views.logout_view, name='logout'),
]
