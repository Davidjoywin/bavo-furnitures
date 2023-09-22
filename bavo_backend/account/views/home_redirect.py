from django.views import View
from django.shortcuts import redirect

class HomeRedirect(View):
    def get(self, request):
        return redirect("product:home")