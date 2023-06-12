from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Category, Order
from .serializers import CategorySerializer, OrderSerializer, TakeOrderSerializer
from .permissions import IsCourier, IsOwnerPermission
from rest_framework.views import APIView
from account.models import User
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'  # Custom query parameter to specify page size
    max_page_size = 100  # Maximum page size allowed


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class OrderViewSet(ModelViewSet):
    
    pagination_class = CustomPagination
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAdminUser, IsOwnerPermission]
        elif self.action == 'retrieve':
            permissions = [IsCourier, IsAdminUser]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]
    
class TakeOrder(APIView):
    def post(self, request):
        order = Order.objects.filter(order_id=request.data.get('order_id')).first()
        serializer = TakeOrderSerializer(context={'order': order}, data=request.data)
        if serializer.is_valid(raise_exception=True):
            order.curier = request.user
            order.save()
            return Response('Ok')
        
    permission_classes = [IsCourier]

     
        
