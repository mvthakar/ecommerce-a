from django.contrib import admin
from .models import Product


class ProductWithFilters(admin.ModelAdmin):
    list_display = ('name', 'price', 'category',)
    search_fields = ('name', 'price',)
    list_filter = ('category',)

admin.site.register(Product, ProductWithFilters)
