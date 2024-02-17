
from africastalking.SMS import SMS
from django.conf import settings

def send_sms(phone_number, message):
    # Initialize Africa's Talking SMS service
    sms = SMS(settings.AT_USERNAME, settings.AT_API_KEY)

    # Send SMS
    try:
        response = sms.send(message, [phone_number])
        # Process response if needed
        print("SMS sent successfully:", response)
        return True
    except Exception as e:
        print("Failed to send SMS:", e)
        return False