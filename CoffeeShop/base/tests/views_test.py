from django.test import TestCase, Client
from django.urls import resolve, reverse
from base.models import Customer, Product, Order
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


class TestEditOrder(TestCase):

    def test_edit_order(self):
        customer = Customer.objects.create(name='alex', served=False)
        product = Product.objects.create( name='something', description='some description', price=1000)
        order = Order.objects.create(customer=customer, product=product, count=1, served=False)
        client = Client()
        response = client.get(reverse('edit_order', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/update_order.html')

