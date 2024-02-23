from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from unittest.mock import patch
from .models import Order

# Mock the send_sms function
def send_sms(phone_number, message):
    pass

class OrderSignalTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='test_user', password='password')

    @patch('<your_app>.utils.send_sms')  # Patch the send_sms function
    def test_send_sms_on_order_added(self, mock_send_sms):
        # Create a sample order
        order = Order.objects.create(item='Test Item', customer=self.user.profile, quantity=1)
        
        # Emit the post_save signal for the Order model
        post_save.send(sender=Order, instance=order, created=True)

        # Assert that the send_sms function was called with the correct arguments
        mock_send_sms.assert_called_once_with(order.customer.phone_number, f"Thank you for your order of {order.item}. Your order has been received!")
