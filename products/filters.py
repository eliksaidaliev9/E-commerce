from django_filters import rest_framework as django_filters
from .models import Product, FlashSale


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']


class FlashSaleFilter(django_filters.FilterSet):
    min_discount = django_filters.NumberFilter(field_name='discount_percentage', lookup_expr='gte')
    max_discount = django_filters.NumberFilter(field_name='discount_percentage', lookup_expr='lte')

    class Meta:
        model = FlashSale
        fields = ['min_discount', 'max_discount']

