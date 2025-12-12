from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from products.models import Product, Category, User

User = get_user_model()


class ProductViewSetTestCase(APITestCase):
    fixtures = ['categories', 'products']

    def setUp(self):
        self.user = User.objects.create_user(phone_number='+998901234567', password='testpass')
        self.staff_user = User.objects.create_user(phone_number='+998909731324', password='staffpass', is_staff=True)
        self.category = Category.objects.first()
        self.product = Product.objects.first()


    def test_product_list(self):
        url = reverse('product-list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)

    def test_product_filter_by_category(self):
        url = reverse('product-list') + '?category=' + str(self.category.id)
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)

    def test_product_detail(self):
        url = reverse('product-detail', args=[self.product.id])
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product']['name'], 'Apple iPhone 17 Pro Max')

    def test_top_rated(self):
        url = reverse('product-top-rated')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Apple iPhone 17 Pro Max')

    def test_average_rating(self):
        url = reverse('product-average-rating', args=[self.product.id])
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data['average_rating'], 4)


    def test_permission_denied_for_anonymous_create(self):
        self.client.force_authenticate(user=None)
        url = reverse('product-list')
        data = {'name': 'Test Product', 'description': 'This is a test product', 'price': 25.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_granted_for_staff(self):
        url = reverse('product-list')
        self.client.force_authenticate(self.staff_user)
        data = {'name': 'Test Product', 'description': 'This is a test product', 'price': 25.00}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)