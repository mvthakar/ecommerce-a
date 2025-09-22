from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def show_login_page(request: HttpRequest):
    return render(request, 'login.html')

def show_signup_page(request: HttpRequest):
    return render(request, 'signup.html')
