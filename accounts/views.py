from django.shortcuts import render, redirect
from allauth.account import views

# Create your views here.

class LoginView(views.LoginView):
  template_name = 'accounts/login.html'
