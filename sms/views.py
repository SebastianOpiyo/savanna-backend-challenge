from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_sms
from .models import Order

@receiver(post_save, sender=Order)
def send_sms_on_order_added(sender, instance, created, **kwargs):
    if created:  
        message = f"Thank you for your order of {instance.item}. Your order has been received!"
        
        # Send the SMS
        phone_number = instance.customer.phone_number  
        send_sms(phone_number, message)

