from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from ..models import Product, Cart
from account.models import Profile


class Home(View):
    def get_object(self, id):
        obj = get_object_or_404(Profile, pk=id)
        return obj
    
    def get(self, request):
        user = request.user
        if request.user.is_authenticated:
            profile = self.get_object(user.id)
            cart = profile.cart
            products = Product.objects.filter(user=profile)

            context = {
                "profile": profile,
                "cart": cart.products.all(),
                "product": products
            }
            return render(request, "index_auth.html")
        else:
            products = Product.objects.all()

            context = {
                "profile": request.user,
                "cart": "",
                "product": products
            }

            return render(request, "index.html")
    
    def post(self, request):
        return redirect('/')
