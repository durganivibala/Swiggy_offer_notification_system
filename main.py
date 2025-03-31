from fetcher import fetch_live_ipl_match
from pollbot import send_poll  # Function to send the chatbot-style poll

def start_daily_notification():
    print("🚀 Checking for today's IPL match...")
    match_link = fetch_live_ipl_match()
    if match_link:
        print("✅ Match found. Sending poll to the user...")
        send_poll(match_link)
    else:
        print("❌ No IPL match found today.")

if __name__ == "__main__":
    start_daily_notification()
