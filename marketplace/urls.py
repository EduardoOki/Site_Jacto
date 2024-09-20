from django.urls import path

from .views import HomeView, ProfileView, ProductView, ProductListView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(),name='profile'),
    path('product/<pk>', ProductView.as_view(),name='product'),
    path('list_product/',ProductListView.as_view(),name='list_product')
]
