from applications.order.models import Order
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
import stripe

from applications.order.serializers import OrderSerializer
from udemy.settings import STRIPE_SECRET_KEY


class OrderApiView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user.id)
        return queryset    
    
        
        
stripe.api_key = STRIPE_SECRET_KEY

class OrderConfirmApiView(APIView):
    def get(self, request, code):
        order = get_object_or_404(Order, activation_code=code)
        
        if not order.is_confirm:
            order.is_confirm = True
            order.status = 'in process'
            order.save(update_fields=['is_confirm', 'status', 'product'])
            return Response({'message': 'You have confirmed order, please tap "POST" to pay'}, status=status.HTTP_200_OK)
        return Response({'message': 'You have already confirmed order'}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, code):
        order = get_object_or_404(Order, activation_code=code)
        amount = int(order.product.price)*100
        token = stripe.Token.create(
  card={
    "number": "4242424242424242",
    "exp_month": 2,
    "exp_year": 2024,
    "cvc": "314",
  },
)
        
        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Example charge',
                source=token,
            )
        except stripe.error.CardError as e:
            return Response({'error': e.json_body['error']['message']}, status=400)
        
        order.status = 'completed'
        order.save(update_fields=['status'])
        return Response({'message': 'Payment successful'}, status=200)    
    
    
    
    



# class PaymentView(APIView):
#     def post(self, request):
#         amount = 1000
#         token = stripe.Token.create(
#   card={
#     "number": "4242424242424242",
#     "exp_month": 2,
#     "exp_year": 2024,
#     "cvc": "314",
#   },
# )
        
#         try:
#             charge = stripe.Charge.create(
#                 amount=amount,
#                 currency='usd',
#                 description='Example charge',
#                 source=token,
#             )
#         except stripe.error.CardError as e:
#             return Response({'error': e.json_body['error']['message']}, status=400)
        
#         return Response({'message': 'Payment successful'}, status=200)    