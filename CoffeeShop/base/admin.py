from django.contrib import admin
from .models import Product,  Customer, Order

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'description', 'price', 'created_at', 'updated_at']
    search_fields = ['name']

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ['name', 'created_at', 'updated_at', 'served']
    list_filter = ['served']
    search_fields = ['name']

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['customer','product', 'count', 'created_at', 'updated_at', 'served']
    list_filter = ['served']

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
