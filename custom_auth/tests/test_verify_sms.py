from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.cache import cache
from rest_framework_simplejwt.tokens import RefreshToken


class VerifySMSTest(APITestCase):
    def setUp(self):
        self.phone = '+998901234567'
        self.code = '1234'
        cache.set(self.phone, self.code)

    def test_verify_sms_success(self):
        url = reverse('verify_sms')
        data = {'phone_number': self.phone, 'verification_code': self.code}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_verify_sms_invalid_code(self):
        url = reverse('verify_sms')
        data = {'phone_number': self.phone, 'verification_code': '9797'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Invalid verification code')