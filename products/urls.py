from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet

from .service.flash_sale import FlashSaleListCreateView, check_flash_sale
from .service.product_view_history import ProductViewHistoryCreate
from .service.product_like import like_product

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('',include(router.urls)),

    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
    path('check-sale/<int:product_id>/', check_flash_sale, name='check-sale'),
    path('product-view/', ProductViewHistoryCreate.as_view(), name='product-view-history-create'),
    path('product-like/<int:product_id>/', like_product, name='like-product'),
]
