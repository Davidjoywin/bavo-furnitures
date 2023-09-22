from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from ..models import Profile

class Register(View):
    def get(self, request):
        ...
    
    def post(self, request):
        password=request.POST.get("password", None)
        verify_password=request.POST.get("verify-password", None)
        email=request.POST.get("email", None)
        username = email.split('@')[0]

        if password == verify_password:
            profile = Profile.objects.create(email=email, username=username)
            profile.set_password(password)
            profile.save()
            print(profile)
            login(request, profile)
            return redirect("/")
        
        return redirect("/")

