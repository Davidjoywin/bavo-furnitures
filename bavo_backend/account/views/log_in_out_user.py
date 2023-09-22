from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from ..models import Profile


class LoginUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("product:home")
        return HttpResponse("Login")
    
    def post(self, request):
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        profile = Profile.objects.get(email=email)
        print(profile)
        if profile.check_password(password):
            login(request, profile)
            return redirect('product:home')
        return redirect('product:home')
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('product:home')