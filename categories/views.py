from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Category


def show_category_list_page(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')
  
  categories = Category.objects.all()
  template_data = {
    "categories": categories
  }
  
  if request.GET.get('error') is not None:
    template_data['error'] = request.GET.get('error')
  
  return render(request, 'list_categories.html', template_data)


def add_category(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')
  
  if request.method == 'GET':
    return show_add_category_page(request)
  
  category_name = request.POST.get('name')
  parent_category_id = request.POST.get('parent-category')

  if category_name is None:
    return render(request, 'add_category.html', {
      'error': 'Category name is required'
    })
  
  parent_category = None
  if parent_category_id != "":
    parent_category = Category.objects.get(id=parent_category_id)

  Category.objects.create(
    name = category_name,
    parent_category = parent_category
  )

  return redirect('add-category')


def show_add_category_page(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')
  
  categories = Category.objects.all().values('id', 'name')
  
  return render(request, 'add_category.html', {
    "categories": categories
  })
  
  
def show_edit_category_page(request: HttpRequest, error: str = None):
  if request.session.get('email') is None:
    return redirect('login')
  
  if error is not None:
    return render(request, 'edit_category.html', {
      "error": error
    })
  
  category_id = request.GET.get('id')
  if category_id is None:
    return redirect("/categories/?error=Category doesnt exist")
  
  category = Category.objects.filter(id=category_id).first()
  if category is None:
    return redirect("/categories/?error=Category doesnt exist")

  all_categories = Category.objects.exclude(id=category_id).values('id', 'name')
  return render(request, 'edit_category.html', {
    "category_to_edit": category,
    "categories": all_categories
  })
  
  
def edit_category(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')
  
  if request.method == "GET":
    return show_edit_category_page(request)

  id = request.POST.get('id')
  name = request.POST.get('name')
  parent_category_id = request.POST.get('parent-category')
  
  category = Category.objects.filter(id=id).first()
  if category is None:
    return show_edit_category_page(request, error="Category doesnt exist")
  
  parent_category = __get_parent_category(parent_category_id)
  if parent_category == "no_id_specified":
    category.name = name
    category.parent_category = None
    category.save()

    return HttpResponse(f"NO ID: {id} - {name} - {parent_category_id}")  
  
  if parent_category is None:
    return show_edit_category_page(request, error="Invalid parent category")

  category.name = name
  category.parent_category = parent_category
  category.save()  

  return HttpResponse(f"With: {id} - {name} - {parent_category_id}")


def delete_category(request: HttpRequest):
  if request.session.get('email') is None:
    return redirect('login')
  
  category_id = request.GET.get('id')
  if category_id is None:
    return redirect("/categories/?error=Category doesnt exist")
  
  category_to_delete = Category.objects.filter(id=category_id)  
  if len(category_to_delete) == 0:
    return redirect("/categories/?error=Category doesnt exist")
  
  category_to_delete.delete()
  return redirect('list-categories')


def __get_parent_category(parent_category_id: str) -> Category | str:
  if parent_category_id is None or parent_category_id == "":
    return "no_id_specified"

  return Category.objects.filter(id=parent_category_id).first()
