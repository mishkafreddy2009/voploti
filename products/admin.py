from django.contrib import admin

from .models import Category, Product, Size

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)