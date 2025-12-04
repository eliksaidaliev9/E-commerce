from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from custom_auth.serializers import SMSSerializer
from custom_auth.services import send_verification_sms


class SendSMSView(APIView):
    @swagger_auto_schema(request_body=SMSSerializer)
    def post(self, request):
        serializer = SMSSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        phone_number = serializer.validated_data['phone_number']
        if send_verification_sms(phone_number):
            return Response({"message": "SMS sent successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Failed to send SMS"}, status=status.HTTP_400_BAD_REQUEST)