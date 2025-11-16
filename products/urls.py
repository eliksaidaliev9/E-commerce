from . import signals
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet, OrderViewSet

from .services.flash_sale import FlashSaleListCreateView, check_flash_sale
from .services.product_view_history import ProductViewHistoryCreate
from .services.product_like import like_product
from .services import admin_replenish_stock

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('',include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('check-sale/<int:product_id>/', check_flash_sale, name='check-sale'),
    path('product-view/', ProductViewHistoryCreate.as_view(), name='product-view-history-create'),
    path('product-like/<int:product_id>/', like_product, name='like-product'),
    path('admin/replenish_stock/<int:product_id>/<int:amount>', admin_replenish_stock, name='admin_replenish_stock'),
]
