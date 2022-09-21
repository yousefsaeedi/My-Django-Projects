from django.test import TestCase
from django.urls import resolve, reverse
import pytest


class TestBaseUrls(TestCase):
    def test_products_url(self):
        path = reverse('products')
        self.assertEqual(resolve(path).view_name, 'products')  

    def test_customers_url(self):
        path = reverse('customers')
        self.assertEqual(resolve(path).view_name, 'customers')

    def test_customer_details_url(self):
        path = reverse('details', kwargs={'pk': 5})
        self.assertEqual(resolve(path).view_name, 'details')  

    def test_orders_url(self):
        path = reverse('orders')
        self.assertEqual(resolve(path).view_name, 'orders')

    def test_create_product_url(self):
        path = reverse('create_product')
        self.assertEqual(resolve(path).view_name, 'create_product')

    def test_create_customer_url(self):
        path = reverse('create_customer')
        self.assertEqual(resolve(path).view_name, 'create_customer')

    def test_update_product_url(self):
        path = reverse('update_product', kwargs={'pk': 6})
        self.assertEqual(resolve(path).view_name, 'update_product')

    def test_update_customer_url(self):
        path = reverse('update_customer', kwargs={'pk': 6})
        self.assertEqual(resolve(path).view_name, 'update_customer')

    def test_delete_product_url(self):
        path = reverse('delete_product', kwargs={'pk': 6})
        self.assertEqual(resolve(path).view_name, 'delete_product')

    def test_delete_customer_url(self):
        path = reverse('delete_customer', kwargs={'pk': 6})
        self.assertEqual(resolve(path).view_name, 'delete_customer')

    def test_customer_order_url(self):
        path = reverse('customer_order', kwargs={'pk': 6})
        self.assertEqual(resolve(path).view_name, 'customer_order')

    def test_create_order_url(self):
        path = reverse('create_order', kwargs={'id': 6, 'pk': 6})
        self.assertEqual(resolve(path).view_name, 'create_order')

    def test_edit_order_url(self):
        path = reverse('edit_order', kwargs={'pk': 6})
        self.assertEqual(resolve(path).view_name, 'edit_order')

    def test_delete_order_url(self):
        path = reverse('delete_order', kwargs={'pk': 6})
        self.assertEqual(resolve(path).view_name, 'delete_order')