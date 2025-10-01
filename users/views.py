from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from .models import User, Role
from utils.validators import email_validator, password_validator

def show_login_page(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'login.html')
        
    return login(request)

def login(request: HttpRequest):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email is None or password is None:
       return render(request, 'login.html', {
           "error": "Email and password are compulsory"
       })
   
    user = User.objects.filter(email=email).first()
    if user is None:
        return render(request, 'login.html', {
           "error": "Wrong email or password"
       })
    
    is_password_valid = check_password(password, user.password_hash)
    if not is_password_valid:
        return render(request, 'login.html', {
           "error": "Wrong email or password"
       })
 
    return redirect('/users/roles')

def show_signup_page(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'signup.html')
    
    return signup(request)

def signup(request: HttpRequest):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    if email is None or password is None:
        return render(request, 'signup.html', {
            "error": "Email and password are compulsory"
        })

    is_email_valid = email_validator.validate(email)
    if not is_email_valid:
        return render(request, 'signup.html', {
            "error": "Invalid email"
        })

    is_password_valid = password_validator.validate(password)
    if not is_password_valid:
        return render(request, 'signup.html', {
            "error": "Password must contain at least 8 characters, 1 capital, 1 small, 1 number, and 1 special char"
        })

    existing_user = User.objects.filter(email=email)
    if existing_user.count() > 0:
        return render(request, 'signup.html', {
            "error": "Sorry, this email is not available"
        })

    customer_role = Role.objects.get(name="Customer")
   
    user = User()
    user.email = email
    user.password_hash = make_password(password)
    user.role = customer_role
    user.save()

    return render(request, 'signup.html', {
        "success": "Signed up successfully"
    })
    
def show_roles_page(request: HttpRequest):
    all_roles = Role.objects.all()
    return render(request, 'roles.html', {
        'roles': all_roles,
        'extra': 'This is a dummy message'
    })
