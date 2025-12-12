from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from django.contrib.auth import get_user_model

from billing.models import Payment
from products.models import Order


User = get_user_model()


class PaymentViewSetTest(APITestCase):
    fixtures = ['users', 'categories', 'products', 'orders', 'payments']

    def setUp(self):
        self.user = User.objects.create_user(phone_number='+998901234567', password='testpass')
        self.staff_user = User.objects.get(phone_number='+998909731324')
        self.client.force_authenticate(user=self.staff_user)
        self.order = Order.objects.first()
        self.payment = Payment.objects.first()


    @patch('billing.views.stripe.Charge.create')
    def test_create_charge_as_staff(self, mock_stripe):
        mock_stripe.return_value ={'id': 'ch_test123'}
        url = reverse('payment-create-charge')
        data = {'order_id': self.order.id, 'stripe_token': 'tok_visa'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('payment', response.data)
        self.assertTrue(Payment.objects.filter(order=self.order).exists())