import requests
from bs4 import BeautifulSoup

def fetch_live_ipl_match():
    url = 'https://www.cricbuzz.com/cricket-match/live-scores'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("❌ Failed to fetch the webpage")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    all_sections = soup.find_all('h2', class_='cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr disp-flex cb-justify-between align-center')
    for section in all_sections:
        if "INDIAN PREMIER LEAGUE" in section.text:
            ipl_block = section.find_next('div', class_='cb-mtch-lst cb-col cb-col-100 cb-tms-itm')
            match = ipl_block.find('h3', class_='cb-lv-scr-mtch-hdr inline-block')
            if match:
                match_link_tag = match.find('a', class_='text-hvr-underline text-bold')
                match_title = match_link_tag.text.strip()
                match_link = 'https://www.cricbuzz.com' + match_link_tag['href']
                print(f"✅ Live IPL Match Found: {match_title}")
                print(f"🔗 Link: {match_link}")
                return match_link
    print("❌ No Live IPL Match Found.")
    return None
