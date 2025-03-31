# detector.py
import requests
from bs4 import BeautifulSoup
import re
from fetcher import fetch_live_ipl_match  #Importing fetcher

def get_recent():
    #Fetch live match URL dynamically
    match_url = fetch_live_ipl_match()
    if not match_url:
        print("❌ No live match URL to fetch recent updates.")
        return None

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(match_url, headers=headers)

    if response.status_code != 200:
        print("❌ Failed to fetch the live match page")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    #Finding the 'Recent' section dynamically
    recent_elem = soup.find('div', class_=re.compile('.*cb-min-rcnt.*'))

    if recent_elem:
        recent_text = recent_elem.get_text(strip=True).replace('Recent:', '').strip()
        print(f"✅ Recent: {recent_text}")
        return recent_text
    else:
        print("⚠️ Could not find the 'Recent' section. Retrying...")
        return None

def check_for_six(recent_text):
    balls = recent_text.split()
    return balls[-1] == '6' if balls else False


