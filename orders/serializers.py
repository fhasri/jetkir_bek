from rest_framework import serializers
from .models import Order, Category



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('phone_sender','phone_receiver','address_sender', 'address_receiver', 'description')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TakeOrderSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()