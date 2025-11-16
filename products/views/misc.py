from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from products.models import Category, Order, Review
from products.serializers import CategorySerializer, OrderSerializer, ReviewSerializer
from products.permissions import IsOwnerOrReadOnly



class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer