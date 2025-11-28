import stripe
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
from decimal import Decimal
from .serializers import PaymentSerializer
from .models import Payment
from products.models import Order
from products.permissions import IsStaffOrReadOnly


stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentViewSet(viewsets.GenericViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=['post'])
    def create_charge(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_id = serializer.validated_data["order_id"]
        stripe_token = serializer.validated_data["stripe_token"]

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            price = order.product.price
            quantity = order.quantity
            total_amount_sum = price * quantity

            usd_exchange_rate = Decimal('11900')
            total_amount_usd = total_amount_sum / usd_exchange_rate
            amount_in_cents = int(total_amount_usd * 100)


            charge = stripe.Charge.create(
                amount=amount_in_cents,
                currency="usd",
                source=stripe_token,
            )

            payment = Payment.objects.create(
                order=order,
                stripe_charge_id=charge["id"],
                amount=total_amount_sum
            )

            order.is_paid = True
            order.save()

            response_data = self.get_serializer(payment).data
            return Response({"status": "Payment successful", "payment": response_data}, status=status.HTTP_200_OK)

        except Exception as e:
            print("ERROR TYPE:", type(e))
            print("ERROR TEXT:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
