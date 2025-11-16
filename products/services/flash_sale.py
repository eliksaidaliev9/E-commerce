from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, serializers, status, filters
from datetime import datetime,timedelta
from products.models import Product, FlashSale, ProductViewHistory

from django_filters import rest_framework as django_filters
from products.filters import FlashSaleFilter
from rest_framework.permissions import IsAuthenticated


class FlashSaleListCreateView(generics.ListCreateAPIView):
    queryset = FlashSale.objects.all()

    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = FlashSaleFilter


    class FlashSaleSerializer(serializers.ModelSerializer):
        class Meta:
            model = FlashSale
            fields = ('id', 'product', 'discount_percentage', 'start_time', 'end_time')

    serializer_class = FlashSaleSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_flash_sale(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"Error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    user_viewed = ProductViewHistory.objects.filter(user=request.user, product=product).exists()

    upcoming_flash_sale = FlashSale.objects.filter(
        product=product,
        start_time__lte=datetime.now() + timedelta(hours=24)
    ).first()

    if user_viewed and upcoming_flash_sale:
        discount = upcoming_flash_sale.discount_percentage
        start_time = upcoming_flash_sale.start_time
        end_time = upcoming_flash_sale.end_time
        return Response({
            "message": f"This product will be on a {discount}% off flash sale!",
            "start_time": start_time,
            "end_time": end_time
        })
    else:
        return Response({
            "message": "No upcoming flash sales for this product."
        })

