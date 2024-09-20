from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
class HomeView(TemplateView):
    template_name = 'marketplace/home.html'

class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = "marketplace/profile.html"

    def get_object(self):
        return super().get_queryset().get(user=self.request.user)
    
class ProductView(generic.DetailView):
    model = Product
    template_name = "marketplace/product.html"

class ProductListView(generic.ListView):
    model = Product
    template_name = "marketplace/list_view.html"
