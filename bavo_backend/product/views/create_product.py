from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from ..models import Product, Cart
from account.models import Profile


class ProductView(View):
    def get_object(self, model, id):
        obj = get_object_or_404(model, pk=id)
        return obj
    
    def get(self, request):
        user = request.user
        print(user.id)
        profile = self.get_object(Profile, 1)
        profile = Profile.objects.get(id=request.user.id)
        cart = self.get_object(Cart, profile.id)
        product = Product.objects.filter(user=profile)

        context = {
            "profile": profile,
            "cart": cart.products.all(),
            "product": product
        }
        return HttpResponse(Profile.objects.get(id=request.user.id))
    
    def post(self, request):
        # proudct = Product.objects.create(**request.POst)
        print(**request.POST)
        return HttpResponse("product create views")
