from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from products.models import Category, Order, Review
from products.serializers import CategorySerializer, OrderSerializer, ReviewSerializer
from products.permissions import IsOwnerOrReadOnly



class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer