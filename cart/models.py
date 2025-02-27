from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE)
    product = models.ForeignKey(User,related_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
