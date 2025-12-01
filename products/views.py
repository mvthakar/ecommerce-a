from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from categories.models import Category
from .models import Product


def show_product_list_page(request: HttpRequest):
    if request.session.get("email") is None:
        return redirect("login")

    products = Product.objects.all()
    return render(request, "list_products.html", {
        "products": products,
    })


def show_add_product_page(request: HttpRequest, error: str = None):
    if request.session.get("email") is None:
        return redirect("login")

    if error is not None:
        return render(request, "add_product.html", {"error": error})

    categories = Category.objects.all().values('id', 'name')
    return render(request, "add_product.html", {
        "categories": categories
    })


def add_product(request: HttpRequest):
    if request.session.get("email") is None:
        return redirect("login")

    if request.method == 'GET':
        return show_add_product_page(request)

    name = request.POST.get("name")
    price = request.POST.get("price")
    category_id = request.POST.get("category")

    if name is None or price is None or category_id is None:
        return render(
            request, "add_product.html", {"error": "All details are required"}
        )

    category = Category.objects.filter(id=category_id).first()
    if category is None:
        return render(request, "add_product.html", {"error": "Invalid category"})

    product = Product()
    product.name = name
    product.price = price
    product.category = category
    product.save()

    return redirect("list-products")


def show_edit_product_page(request: HttpRequest, error: str = None):
    if request.session.get("email") is None:
        return redirect("login")

    if error is not None:
        return render(request, "edit_product.html", {"error": error})

    id = request.GET.get("id")
    if id is None:
        return redirect("list-products")

    product = Product.objects.filter(id=id).first()
    if product is None:
        return redirect("list-products")

    categories = Category.objects.all().values('id', 'name')
    return render(request, "edit_product.html", {
        "categories": categories,
        "product": product
    })


def edit_product(request: HttpRequest):
    if request.session.get("email") is None:
        return redirect("login")

    if request.method == 'GET':
        return show_edit_product_page(request)

    id = request.POST.get("id")
    name = request.POST.get("name")
    price = request.POST.get("price")
    category_id = request.POST.get("category")

    if id is None or name is None or price is None or category_id is None:
        return render(request, "edit_product.html", {"error": "All details are required"})

    product = Product.objects.filter(id=id).first()
    if product is None:
        return render(request, "edit_product.html", {"error": "Invalid product"})

    category = Category.objects.filter(id=category_id).first()
    if category is None:
        return render(request, "edit_product.html", {"error": "Invalid category"})

    product.name = name
    product.price = price
    product.category = category
    product.save()

    return redirect("list-products")


def delete_product(request: HttpRequest):
    if request.session.get("email") is None:
        return redirect("login")

    id = request.GET.get("id")
    if id is None:
        return redirect("list-products")

    product = Product.objects.filter(id=id).first()
    if product is None:
        return redirect("list-products")

    product.delete()
    return redirect("list-products")
