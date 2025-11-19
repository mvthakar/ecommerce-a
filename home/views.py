from django.http import HttpRequest
from django.shortcuts import render, redirect


def show_home_page(request: HttpRequest):
    if request.session.get('email') is None:
        return redirect('login')
    
    return render(request, 'home.html')
