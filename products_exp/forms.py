from django import forms
from products.models import Product


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"},),
            "price": forms.TextInput(attrs={"class": "form-control"},),
            "category": forms.Select(attrs={"class": "form-select"}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

