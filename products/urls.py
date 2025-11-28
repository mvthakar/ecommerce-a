from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_product_list_page, name='list-products'),
    path('add/', views.add_product, name='add-product'),
    path('edit/', views.edit_product, name='edit-product'),
    path('delete/', views.delete_product, name='delete-product'),
]
