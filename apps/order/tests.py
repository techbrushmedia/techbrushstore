from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.product.models import Product
from .models import Address, Order


class OrderAccessTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            name='Test Customer',
            email='customer@example.com',
            phone='0123456789',
            district='Dhaka',
            address='1 Test Street',
        )

    def test_guest_confirmation_requires_the_original_session(self):
        order = Order.objects.create(
            subtotal=100,
            total_amount=100,
            address=self.address,
        )
        url = reverse('confirmation', kwargs={'order_number': order.order_number})

        self.assertEqual(self.client.get(url).status_code, 404)

        session = self.client.session
        session[f'order_access_{order.order_number}'] = str(order.access_token)
        session.save()
        self.assertEqual(self.client.get(url).status_code, 200)

    def test_order_cancellation_requires_post(self):
        user = get_user_model().objects.create_user(
            username='testcustomer',
            email='testcustomer@example.com',
            phone='0123456789',
            password='strong-test-password',
        )
        product = Product.objects.create(
            name='Test Product',
            price=100,
            sku='TEST-001',
            stock_quantity=3,
        )
        order = Order.objects.create(
            user=user,
            subtotal=100,
            total_amount=100,
            address=self.address,
        )
        self.client.force_login(user)
        url = reverse('cancel_order', kwargs={'order_number': order.order_number})

        self.assertEqual(self.client.get(url).status_code, 405)
        self.assertEqual(self.client.post(url).status_code, 302)
        order.refresh_from_db()
        self.assertEqual(order.status, 'cancelled')
