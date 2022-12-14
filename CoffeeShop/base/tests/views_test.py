from django.test import TestCase, Client, RequestFactory
from django.urls import resolve, reverse
from base.models import Customer, Product, Order
from base.views import customerOrder
from base.forms import OrderForm
import pytest


class ProductListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='john', served=False)
        # Create 11 products
        number_of_products = 11
        for product_id in range(number_of_products):
            Product.objects.create(
                name=f'product number {product_id}',
                description=f'description  {product_id}',
                price=1000
            )

    def get_context_data(self, **kwargs):
        context = super(ProductListViewTest, self).get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context

    def test_get_context_data(self):
        response = self.client.get('/')
        self.assertTrue('customers' in response.context)

class OrderListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(name='john', served=False)
        # Create 11 products
        number_of_products = 11
        for product_id in range(number_of_products):
            Product.objects.create(
                name=f'product number {product_id}',
                description=f'description  {product_id}',
                price=1000
            )

    def get_context_data(self, **kwargs):
        context = super(OrderListViewTest, self).get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context

    def test_get_context_data(self):
        response = self.client.get('/orders/')
        self.assertTrue('customers' in response.context)


class TestEditOrder(TestCase):

    def test_edit_order(self):
        customer = Customer.objects.create(name='alex', served=False)
        product = Product.objects.create( name='something', description='some description', price=1000)
        order = Order.objects.create(customer=customer, product=product, count=1, served=False)
        client = Client()
        response = client.get(reverse('edit_order', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/update_order.html')

class TestCustomerOrder(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.not_ordered_customer = Customer.objects.create(name='ali')
        self.ordered_customer = Customer.objects.create(name='john', served=False)
        # Create 11 products
        number_of_products = 11
        for product_id in range(number_of_products):
            Product.objects.create(
                name=f'product number {product_id}',
                description=f'description  {product_id}',
                price=1000
            )
        self.order1 = Order.objects.create(customer_id=2, product_id=1, count=2, served=True)
        self.order2 = Order.objects.create(customer_id=2, product_id=2, count=1, served=True)
        self.order3 = Order.objects.create(customer_id=2, product_id=3, count=4, served=False)
        self.orders = [self.order1.served, self.order2.served, self.order3.served]
        self.customers = Customer.objects.all()

    def test_customer_order_url(self):
        order1 = self.order1
        response = self.client.get(reverse('customer_order', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_not_ordered_customer(self):
        request = self.factory.get('/customer-order/2/')
        response = customerOrder(request, 2)
        self.assertEqual(response.status_code, 200)

class TestCreateOrder(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        Customer.objects.create(name='yousef')
        Product.objects.create(name='something', description='blahblah blah', price=1000)
        self.order1 = Order.objects.create(customer_id=1, product_id=1, count=1)
        self.order2 = Order.objects.create(customer_id=1, product_id=1, count=2)

    def test_create_order_url(self):
        order = self.order1
        response = self.client.get(reverse('create_order', args=[1, 1]))
        self.assertEqual(response.status_code, 200)

    def test_form_post(self):
        response = self.client.post("/create-order/1/1/")
        self.assertEqual(response.status_code, 200)

    def test_form_get(self):
        response = self.client.get("/create-order/1/1/")
        self.assertEqual(response.status_code, 200)
