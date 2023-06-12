from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CategoryViewSet, TakeOrder

router = DefaultRouter()

router.register('orders', OrderViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('curier/', TakeOrder.as_view())
]