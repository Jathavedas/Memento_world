# forms.py
from django import forms
from .models import Items

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'type', 'price', 'stock', 'image']
