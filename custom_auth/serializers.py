from rest_framework import serializers
import re


class SMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)

    def validate_phone_number(self, value):
        pattern = r'^\+?\d{9,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("The phone number is in the wrong format.")
        return value


class VerifySMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    verification_code = serializers.CharField(max_length=6, min_length=4)

    def validate_phone_number(self, value):
        pattern = r'^\+?\d{9,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("The phone number is in the wrong format.")
        return value