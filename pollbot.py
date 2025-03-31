from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import subprocess
import os

app = Flask(__name__)

#Twilio Credentials
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')
user_number = os.getenv('USER_NUMBER')  # Replace with your WhatsApp number

client = Client(account_sid, auth_token)

#Function to send poll message to the user
def send_poll(match_title):
    poll_message = f"🏏 IPL Match Today: {match_title}\nReceive notifications whenever there is a 6 and avail 66% offer from swiggy\n\nReply with:\n👉 START - To Receive Alerts\n👉 STOP - To Skip Alerts"
    message = client.messages.create(
        from_=twilio_whatsapp_number,
        body=poll_message,
        to=user_number
    )
    print("✅ Poll sent to user")

#Route to handle incoming replies (START/STOP)
@app.route("/incoming", methods=['POST'])
def incoming_sms():
    incoming_msg = request.values.get('Body', '').strip().upper()
    print(f"📩 User replied: {incoming_msg}")
    resp = MessagingResponse()

    if incoming_msg == 'START':
        resp.message("✅ Monitoring started! You'll receive SIX notifications.")
        # Start the notifier.py monitoring in the background
        subprocess.Popen(["python", "notifier.py"])
    elif incoming_msg == 'STOP':
        resp.message("❌ Monitoring stopped. No notifications will be sent.")
    else:
        resp.message("⚠️ Invalid response. Please reply with 'START' or 'STOP'.")

    return str(resp)


