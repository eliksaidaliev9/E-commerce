from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch


class SendSMSTest(APITestCase):
    @patch('custom_auth.views.send_sms.send_verification_sms')
    def test_send_sms_success(self, mock_send):
        mock_send.return_value = True
        url = reverse('send_sms')
        data = {'phone_number': '+998901234567'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'SMS sent successfully')
        mock_send.assert_called_once()


    @patch('custom_auth.views.send_sms.send_verification_sms')
    def test_send_sms_fail(self, mock_send):
        mock_send.return_value = False
        url = reverse('send_sms')
        data = {'phone_number': '+998901234567'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Failed to send SMS')