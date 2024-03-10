from django.urls import path

from .views import product_detail

urlpatterns = [
    path('product/<slug>', product_detail, name='product-detail'),
]
