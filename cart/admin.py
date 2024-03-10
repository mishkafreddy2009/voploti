from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    model = Customer

admin.site.register(Customer, CustomerAdmin)