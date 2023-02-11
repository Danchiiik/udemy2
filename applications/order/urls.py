from django.urls import path, include
from applications.order.views import OrderApiView, OrderConfirmApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', OrderApiView)

urlpatterns = [
    path('confirm/<uuid:code>/', OrderConfirmApiView.as_view()),
    path('', include(router.urls))
]