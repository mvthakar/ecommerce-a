from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_product_list_page, name='list-products-exp'),
    path('add/', views.add_product, name='add-product-exp'),
    path('edit/', views.edit_product, name='edit-product-exp'),
    path('delete/', views.delete_product, name='delete-product-exp'),
    path('contact/', views.show_contact_page, name='contact-exp'),
]
