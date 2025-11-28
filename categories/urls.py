from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_category_list_page, name='list-categories'),
    path('add/', views.add_category, name='add-category'),
    path('edit/', views.edit_category, name='edit-category'),
    path('delete/', views.delete_category, name='delete-category'),
]
