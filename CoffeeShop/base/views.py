from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import OrderForm, OrderUpdateForm
from .models import Product, Customer, Order

# =========================== General CRUD Operations ==============================
class ProductList(ListView):
    model = Product
    template_name = 'base/products.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()[:11]
        return context

class CustomerList(ListView):
    model = Customer
    template_name = 'base/Customers.html'
    context_object_name = 'customers'

class CustomerDetails(DetailView):
    model = Customer
    template_name = 'base/customer_details.html'
    context_object_name = 'customer'

class OrderList(ListView):
    model = Order
    template_name = 'base/orders.html'
    context_object_name = 'orders'
    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context

class CreateProduct(CreateView):
    model = Product
    fields = '__all__'
    context_object_name = 'form'
    success_url = reverse_lazy('products')
    template_name = 'base/create_product.html'

class CreateCustomer(CreateView):
    model = Customer
    fields = ['name']
    context_object_name = 'form'
    success_url = reverse_lazy('products')
    template_name = 'base/create_customer.html'

class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'
    context_object_name = 'form'
    success_url = reverse_lazy('products')
    template_name = 'base/create_product.html'

class UpdateCustomer(UpdateView):
    model = Customer
    fields = ['name']
    context_object_name = 'form'
    success_url = reverse_lazy('products')
    template_name = 'base/create_customer.html'

class DeleteProduct(DeleteView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products')

class DeleteCustomer(DeleteView):
    model = Customer
    context_object_name = 'customer'
    success_url = reverse_lazy('products')

# ============================ To Order Part ==============================

def customerOrder(request, pk):
    total_cost = 0
    customer_orders_served = []
    customer = Customer.objects.get(id=pk)
    orders = Order.objects.filter(customer=customer)
    products = Product.objects.all()
    # Calculate The Total Cost For Customer's Orders
    if orders.__len__() == 0:
        customer.served = False
        customer.save()
        context = {
            'customer': customer,
            'orders': orders,
            'products': products,
            'total_cost': total_cost,
        }
        return render(request, 'base/customer_order.html', context)
    else:
        for order in orders:
            order_cost = order.count * order.product.price
            total_cost += order_cost
            customer_orders_served.append(order.served)
        if all(customer_orders_served):
            customer.served = True
            customer.save()
        else:
            customer.served = False
            customer.save()
        context = {
            'customer': customer,
            'orders': orders,
            'products': products,
            'total_cost': total_cost,
        }
        return render(request, 'base/customer_order.html', context)

# ====================== Add New Order ============================

def createOrder(request, id, pk):
    customer = Customer.objects.get(id=id)
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.product = product
            new_order.count = request.POST.get('count')
            new_order.save()
            return HttpResponseRedirect(reverse('customer_order', kwargs={'pk': customer.id}))
    else:
        form = OrderForm(initial={'customer': customer, 'product': product, 'count': 1})
    return render(request, 'base/create_order.html', {'form': form, 'customer': customer})

# ====================== Update & Delete Order ==============================

def editOrder(request, pk):
    order = Order.objects.get(id=pk)
    count = order.count
    product = Product.objects.get(id=order.product.id)
    customer = Customer.objects.get(id=order.customer.id)
    served = order.served

    if request.method == 'POST':
        form = OrderUpdateForm(request.POST)
        if form.is_valid():
            Id = order.id
            order.delete()
            new_order = form.save(commit=False)
            new_order.id = Id
            new_order.customer = customer
            new_order.count = request.POST.get('count')
            new_order.served = request.POST.get('served')
            if new_order.served == "on":
                new_order.served = True
            else:
                new_order.served = False
            new_order.save()
            return HttpResponseRedirect(reverse('customer_order', kwargs={'pk': customer.id}))
    else:
        form = OrderUpdateForm(initial={'product': product, 'count': count, 'served': served})
    return render(request, 'base/update_order.html', {'form': form , 'customer': customer})

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    customer = Customer.objects.get(id=order.customer.id)
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('customer_order', kwargs={'pk': customer.id}))
    return render(request, 'base/order_confirm_delete.html', {'order': order, 'customer': customer})    
