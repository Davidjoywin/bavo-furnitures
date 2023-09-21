from django.urls import path

from .views import *


urlpatterns = [
    path("home", Home.as_view(), name="name"),
    path("add-to-cart", AddToCart.as_views(), name="add-to-cart")
]