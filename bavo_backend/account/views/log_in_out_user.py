from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from ..models import Profile


class LoginUser(View):
    def get(self, request):
        return HttpResponse("successful render")
    
    def post(self, request):
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect("main:app")
        return redirect("auth:login")
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("main:app")