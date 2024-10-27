from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "index.html")

def loginview(request):
    if request.method == "POST":
        usname = request.POST.get("username")
        passw = request.POST.get("password")
        user = authenticate(request, username=usname, password=passw)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid details")
            return render(request, "login.html")
    return render(request, "login.html")
