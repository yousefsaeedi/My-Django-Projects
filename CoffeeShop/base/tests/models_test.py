from django.test import TestCase
from base.models import Product, Customer, Order
from django.urls import resolve, reverse
import pytest


class TestBaseModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product = Product.objects.create(name='first_product')
        cls.customer = Customer.objects.create(name='first_customer')
        cls.order = Order.objects.create(customer=cls.customer, product=cls.product)


    def test_product_model_str(self):
        self.assertEqual(str(self.product), 'first_product')
        
    def test_customer_model_str(self):
        self.assertEqual(str(self.customer), 'first_customer')

    def test_order_model_str(self):
        self.assertEqual(str(self.order), 'first_product')

