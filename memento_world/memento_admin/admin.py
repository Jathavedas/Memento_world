# In admin.py
from django.contrib import admin
from .models import Type, Items

class Typeadm(admin.ModelAdmin):
    list_display = ['type']  # Only fields that actually exist on Type

class Itemsadm(admin.ModelAdmin):
    list_display = ['name', 'type', 'price', 'stock', 'image']  # These fields exist on Items

admin.site.register(Type, Typeadm)
admin.site.register(Items, Itemsadm)
