import time
import datetime
from fetcher import fetch_live_ipl_match
from pollbot import send_poll  # Function to send the chatbot-style poll

def start_daily_notification():
    """Send a poll if an IPL match is happening today."""
    print("🚀 Checking for today's IPL match...")
    match_link = fetch_live_ipl_match()
    if match_link:
        print("✅ Match found. Sending poll to the user...")
        send_poll(match_link)
    else:
        print("❌ No IPL match found today.")

def is_within_time_range():
    """ Check if the current time is between 7:30 PM and 11:00 PM """
    now = datetime.datetime.now()
    start_time = now.replace(hour=19, minute=30, second=0, microsecond=0)  # 7:30 PM
    end_time = now.replace(hour=23, minute=0, second=0, microsecond=0)  # 11:00 PM
    return start_time <= now <= end_time

if __name__ == "__main__":
    while True:
        current_time = datetime.datetime.now()
        
        if current_time.hour == 19 and current_time.minute == 30:
            start_daily_notification()
        
        if current_time.hour >= 23:
            print("⏸️ Stopping the script for today. Restarting tomorrow...")
            break  # Stop the script after 11 PM
        
        time.sleep(60)  # Check every minute

