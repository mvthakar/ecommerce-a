from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def show_login_page(request: HttpRequest):
    if request.method == 'GET':
        return __handle_login_get(request)

    email = request.POST['email']
    password = request.POST['password']
    
    if email == '' or password == '':
        return HttpResponse('Email and password are compulsory')
    
    if email != "admin@gmail.com" or password != "Admin@1234":
        return HttpResponse('Wrong email or password')    

    response = HttpResponse('Logged in')
    response.set_cookie(
        key='email',
        value=email
    )
    
    return response

def show_signup_page(request: HttpRequest):
    return render(request, 'signup.html')

def __handle_login_get(request: HttpRequest):
    loggedInEmail = request.COOKIES.get('email')
    if loggedInEmail is None:
        return render(request, 'login.html')
    
    return HttpResponse(f"Welcome, {loggedInEmail}")
