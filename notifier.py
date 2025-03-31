import time
from detector import get_recent, check_for_six
from twilio.rest import Client
import os

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
user_number = os.getenv('USER_NUMBER')

client = Client(account_sid, auth_token)

def send_six_alert():
    message = "🔥🔥 SIX HIT in the IPL match!"
    client.messages.create(
        from_=twilio_whatsapp_number,
        body=message,
        to=user_number
    )
    print("✅ SIX Notification sent!")

def start_monitoring():
    print("🚀 Monitoring started for SIX alerts...")
    last_event = None
    while True:
        recent_text = get_recent()
        if recent_text and recent_text != last_event:
            last_event = recent_text
            if check_for_six(recent_text):
                send_six_alert()
        time.sleep(120)  # ✅ Check every 2 mins


