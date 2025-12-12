from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from rest_framework.test import APITestCase
from rest_framework import status

from products.models import Order, Product
from products.signals import notify_admin


post_save.disconnect(notify_admin, sender=Order)

User = get_user_model()


class OrderViewSetTests(APITestCase):
    fixtures = ['users', 'categories', 'products', 'orders']

    def setUp(self):
        self.user = User.objects.create_user(phone_number='+998901234567', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.order = Order.objects.first()
        self.product = Product.objects.first()

        self.order.customer = self.user
        self.order.save()

    def test_order_list(self):
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_order_detail(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.order.id)

    def test_order_create(self):
        url = reverse('order-list')
        data = {'product': self.product.id, 'customer': self.user.id, 'quantity': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order_update(self):
        url = reverse('order-detail', args=[self.order.id])
        data = {'product': self.product.id, 'customer': self.user.id, 'quantity': 1}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_delete(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)