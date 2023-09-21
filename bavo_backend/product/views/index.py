from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from ..models import Product, Cart
from account.models import Profile


class Home(View):
    def get_object(self, model, id):
        obj = get_object_or_404(model, pk=id)
        return obj
    
    def get(self, request):
        user = request.user
        profile = self.get_object(profile, user.id)
        cart = self.get_object(Cart, id)
        product = Product.objects.filter(user=profile)

        context = {
            "profile": profile,
            "cart": cart.products.all(),
            "product": product
        }
        return HttpResponse("Homepage")
    
    def post(self, request):
        return HttpResponse("home page ")
