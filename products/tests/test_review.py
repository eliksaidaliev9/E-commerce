from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from products.models import Review, Product

User = get_user_model()


class ReviewViewSetTestCase(APITestCase):
    fixtures = ['users', 'categories', 'products', 'reviews']

    def setUp(self):
        self.user = User.objects.create_user(phone_number='+998901234567', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.review = Review.objects.first()
        self.product = Product.objects.first()

    def test_review_list(self):
        url = reverse('review-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_review_detail(self):
        url = reverse('review-detail', args=[self.review.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_create(self):
        url = reverse('review-list')
        data = {'user': self.user.id, 'product': self.product.id, 'content': 'super', 'rating': 5}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_review_update(self):
        url = reverse('review-detail', args=[self.review.pk])
        data = {'user': self.user.id, 'product': self.product.id, 'content': 'super', 'rating': 3}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_delete(self):
        url = reverse('review-detail', args=[self.review.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
