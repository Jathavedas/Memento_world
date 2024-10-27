from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from memento_admin.models import Items, Type


def home(request):
    return render(request, "home.html")


def view_trophy(request):
    memento_type = Type.objects.filter(type='trophy').first()
    if memento_type:
        items = Items.objects.filter(type=memento_type)
        return render(request, 'view_trophy.html', {'trophy': items})  # Render the template with the items


def view_memento(request):
    memento_type = Type.objects.filter(type='memento').first()
    if memento_type:
        items = Items.objects.filter(type=memento_type)
        return render(request, 'view_memento.html', {'memento': items}) 
