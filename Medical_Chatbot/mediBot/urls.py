from django.urls import path
from . import views

urlpatterns = [
    path('adminLogin/', views.adminLogin, name='adminLogin'),
]
