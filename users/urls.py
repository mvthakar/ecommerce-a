from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.show_login_page),
    path('signup/', views.show_signup_page),
]
