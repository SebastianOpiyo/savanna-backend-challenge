from django.db import models
from django.contrib.auth.models import User  # If you're using Django's built-in User model

class SMSMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'SMS to {self.phone_number} at {self.timestamp}'
    

