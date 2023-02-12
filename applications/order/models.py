import uuid
from django.db import models
from django.contrib.auth import get_user_model

from applications.product.models import Course

User = get_user_model()

class Order(models.Model):
    STATUS = (
        ('in process', 'in process'),
        ('completed', 'completed'),
        ('canceled', 'canceled')
    )
    
    product = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='orders')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=50, choices=STATUS, null=True, blank=True)
    is_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    activation_code = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self) -> str:
        return f'{str(self.owner)} - {str(self.product.title)}'
    