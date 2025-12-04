from django.urls import path
from .views import SendSMSView, VerifySMSView


urlpatterns = [
    path('send-sms/', SendSMSView.as_view(), name='send_sms'),
    path('verify-sms/', VerifySMSView.as_view(), name='verify_sms'),
]