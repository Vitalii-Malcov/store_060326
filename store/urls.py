from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (ProductListViewSet,
                    ProductDetailUpdateViewSet,
                    ProductDetailListCreateViewSet,
                    ProductDetailDetailUpdateDeleteViewSet, AddressViewSet,
                    CustomerListCreateViewSet, CustomerDetailUpdateDeleteViewSet,
                    OrderListCreateViewSet, OrderDetailUpdateDeleteView,
                    OrderItemListCreateViewSet, OrderItemDetailUpdateDeleteView

                    )
from .views import (
    CategoryViewSet,
    SupplierViewSet,

)

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('supplier', SupplierViewSet)
router.register('address', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListViewSet.as_view()),
    path('products/<int:pk>/', ProductDetailUpdateViewSet.as_view()),
    path('product-details/', ProductDetailListCreateViewSet.as_view()),
    path('product-details/<int:pk>/', ProductDetailDetailUpdateDeleteViewSet.as_view()),
    path('customers/', CustomerListCreateViewSet.as_view()),
    path('customers/<int:pk>/', CustomerDetailUpdateDeleteViewSet.as_view()),
    path('orders/', OrderListCreateViewSet.as_view()),
    path('orders/<int:pk>/', OrderDetailUpdateDeleteView.as_view()),
    path('order-items/', OrderItemListCreateViewSet.as_view()),
    path('order-items/<int:pk>/', OrderItemDetailUpdateDeleteView.as_view()),

]