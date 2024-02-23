from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_sms
from .models import Order

@receiver(post_save, sender=Order)
def send_sms_on_order_added(sender, instance, created, **kwargs):
    if created:  # Check if the order was just created
        # Customize the message as per your requirement
        message = f"Thank you for your order of {instance.item}. Your order has been received!"
        
        # You may get the phone number from the associated customer or however you manage it
        phone_number = instance.customer.phone_number  # Assuming customer has a phone_number field

        # Call the send_sms function from utils.py to send the SMS
        send_sms(phone_number, message)

