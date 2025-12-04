from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import APIView, swagger_auto_schema
from drf_yasg import openapi
from custom_auth.serializers import VerifySMSSerializer

User = get_user_model()

class VerifySMSView(APIView):
    @swagger_auto_schema(request_body=VerifySMSSerializer)
    def post(self, request):
        serializer = VerifySMSSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        phone_number = serializer.validated_data['phone_number']
        verification_code = serializer.validated_data['verification_code']

        cached_code = cache.get(phone_number)
        if cached_code is None or cached_code != verification_code:
            return Response({"message": "Invalid verification code"}, status=status.HTTP_400_BAD_REQUEST)

        user, created = User.objects.get_or_create(phone_number=phone_number)
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            },
            status=status.HTTP_200_OK
        )
