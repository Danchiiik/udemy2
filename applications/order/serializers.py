from django.conf import settings
from rest_framework import serializers
import stripe

from applications.order.models import Order
from applications.order.tasks import send_confirmation_code


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
   
    class Meta:
        model = Order
        exclude = ['activation_code', 'is_confirm']
                     
    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        send_confirmation_code.delay(order.owner.email, order.activation_code)
        return order
    
