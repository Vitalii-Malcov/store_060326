from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializer import OrderCrateUpdateSerializer, OrderItemCrateUpdateSerializer
from .serializer import CustomerCreateUpdateSerializer
from .serializer import ProductCreateUpdateSerializer
from .models import Category, Supplier, Product, ProductDetail, Address, Customer, Order, OrderItem
from .serializer import (
                    CategorySerializer,
                    CustomerSerializer,
                    AddressSerializer,
                    OrderSerializer,
                    OrderItemSerializer,
                    ProductSerializer,
                    ProductDetailSerializer,
                    ProductDetailCreateUpdateSerializer,
                    SupplierSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductListViewSet(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer

class ProductDetailUpdateViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductCreateUpdateSerializer


class ProductDetailListCreateViewSet(ListCreateAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer


class ProductDetailDetailUpdateDeleteViewSet(RetrieveUpdateDestroyAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductDetailSerializer
        return ProductDetailCreateUpdateSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CustomerListCreateViewSet(ListCreateAPIView):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer

class CustomerDetailUpdateDeleteViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        return CustomerCreateUpdateSerializer

class OrderListCreateViewSet(ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCrateUpdateSerializer


class OrderDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        return OrderCrateUpdateSerializer

class OrderItemListCreateViewSet(ListCreateAPIView):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCrateUpdateSerializer


class OrderItemDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderItemSerializer
        return OrderItemCrateUpdateSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'price']
    # get_serializer_class оставить как был


class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']
    # get_serializer_class оставить как был

