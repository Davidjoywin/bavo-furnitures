from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Profile


def register(request):
    if request.method == 'POST':
        username=request.POST.get("username", None)
        password=request.POST.get("password", None)
        verify_password=request.POST.get("verify-password", None)
        email=request.POST.get("email", None)
        first_name=request.POST.get("first-name", None)
        last_name=request.POST.get("last-name", None)

        if password == verify_password:
            profile = Profile.objects.create(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name
            )
            profile.save()
            login(request, profile)
            return redirect("main:app")
        
        return redirect("account:register")

    return HttpResponse("successful render")

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect("main:app")
        return redirect("auth:login")
    return HttpResponse("successful render")

def logout_user(request):
    logout(request)
    return redirect("auth:login")

        