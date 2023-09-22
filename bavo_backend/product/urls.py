from django.urls import path

from .views import *

app_name = 'product'
urlpatterns = [
    path("home", Home.as_view(), name="home"),
    path("create", ProductView.as_view(), name="create-product"),
    path("<int:product_id>/add", AddToCart.as_view(), name="add-to-cart"),
    path("<int:product_id>/remove", RemoveFromCart.as_view(), name="remove-from-cart"),
]