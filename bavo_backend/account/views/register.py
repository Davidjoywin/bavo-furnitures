from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from ..models import Profile

class Register(View):
    def get(self, request):
        return HttpResponse("successful render")
    
    def post(self, request):
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

