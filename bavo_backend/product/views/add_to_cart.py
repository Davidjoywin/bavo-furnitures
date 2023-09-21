from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from ..models import Product, Cart
from account.models import Profile


class AddToCart(View):
    def get_object(self, model, id):
        obj = get_object_or_404(model, pk=id)
        return obj
    
    def post(self, request, product_id):
        user = request.user
        profile = self.get_object(Profile, user.id)
        product = self.get_object(Product, product_id)
        cart = self.get_object(Cart, profile.id)

        cart.products.add(product)
        return HttpResponse("Product added successfully!")