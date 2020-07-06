from django import forms
from .models import Product

class ProductForm(forms.Model):
    class Meta:
        model = Productfields = [
            'title',
            'description',
            'price'
        ]