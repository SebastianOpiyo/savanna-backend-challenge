from django.db import models
from customers.models import Customer

# Create your models here.
class Order(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ForeignKey relationship
    status = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product