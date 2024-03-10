import uuid
from django.shortcuts import render

from products.models import Product, Category
from cart.models import Customer


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category')

    if active_category:
        products = Product.objects.filter(category__slug=active_category)

    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category,
    }

    response = render(request, 'core/index.html', context)

    return response
    # return response.set_cookie('device', device)