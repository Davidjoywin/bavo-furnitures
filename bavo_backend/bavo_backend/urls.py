from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from account.views import HomeRedirect

favicon_view = RedirectView.as_view(url='static/images/g1.png', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeRedirect.as_view(), name='home-redirect'),
    path("account/", include("account.urls")),
    path("product/", include("product.urls")),
    path('favicon.ico/', favicon_view),
]
