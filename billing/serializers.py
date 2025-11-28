from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    order_id = serializers.IntegerField(write_only=True)
    stripe_token = serializers.CharField(write_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'order', 'stripe_charge_id', 'amount', 'created_at', 'order_id', 'stripe_token']
        read_only_fields = ['id', 'order', 'stripe_charge_id', 'amount', 'created_at']