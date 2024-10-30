from django import forms
from .models import Product, Contact

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"