# 
from django.db import models
from django.contrib.auth import get_user_model
from orders.models import Order

User = get_user_model()

class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
class RatingUser(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_ratings')
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.rating)
