from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password

from .models import User, Role

def show_login_page(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'login.html')
        
    return login(request)

def login(request: HttpRequest):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email is None or password is None:
       return HttpResponse("Email and password are compulsory")
   
    user = User.objects.filter(email=email).first()
    if user is None:
        return HttpResponse("Wrong email or password")
    
    is_password_valid = check_password(password, user.password_hash)
    if not is_password_valid:
        return HttpResponse("Wrong email or password")
 
    return HttpResponse("Logged in successfully")    

def show_signup_page(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'signup.html')
    
    return signup(request)

def signup(request: HttpRequest):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email is None or password is None:
       return HttpResponse("Email and password are compulsory")

    existing_user = User.objects.get(email=email)
    if existing_user is not None:
        return HttpResponse("Sorry, this email is not available")

    customer_role = Role.objects.get(name="Customer")
   
    user = User()
    user.email = email
    user.password_hash = make_password(password)
    user.role = customer_role
    
    user.save()
    return HttpResponse("Signed up successfully")
    