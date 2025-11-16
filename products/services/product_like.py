from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, serializers
from products.serializers import ProductLikeSerializer
from products.models import Product, ProductLike


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExists:
        return Response({"Error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    like, created = ProductLike.objects.get_or_create(user=request.user, product=product)
    serializer = ProductLikeSerializer(like)

    if created:
        return Response({
            "message": "You liked this product:",
            "like": serializer.data
        }, status=status.HTTP_200_OK)
    return Response({
        "message": "You already liked this product.",
        "like": serializer.data
    }, status=status.HTTP_200_OK)
