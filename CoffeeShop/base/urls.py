from django.urls import path
from .views import (ProductList, CustomerList, CustomerDetails, OrderList,
                    CreateProduct, CreateCustomer,
                    UpdateProduct, UpdateCustomer,
                    DeleteProduct, DeleteCustomer,
                    customerOrder, createOrder, 
                    deleteOrder, editOrder)


urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('customers/', CustomerList.as_view(), name='customers'),
    path('customer-details/<int:pk>/', CustomerDetails.as_view(), name='details'),
    path('orders/', OrderList.as_view(), name='orders'),

    path('create-product/', CreateProduct.as_view(), name='create_product'),
    path('create-customer/', CreateCustomer.as_view(), name='create_customer'),
    path('update-product/<int:pk>/', UpdateProduct.as_view(), name='update_product'),
    path('update-customer/<int:pk>/', UpdateCustomer.as_view(), name='update_customer'),
    path('delete-product/<int:pk>/', DeleteProduct.as_view(), name='delete_product'),
    path('delete-customer/<int:pk>/', DeleteCustomer.as_view(), name='delete_customer'),

    path('customer-order/<int:pk>/', customerOrder, name='customer_order'),
    path('create-order/<int:id>/<int:pk>/', createOrder, name='create_order'),
    path('edit-order/<int:pk>/', editOrder, name='edit_order'),
    path('delete-order/<int:pk>/', deleteOrder, name='delete_order'),
]