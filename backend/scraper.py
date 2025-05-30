
import requests
from bs4 import BeautifulSoup

def scrape_jobs(query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    search_url = f"https://www.google.com/search?q=site:linkedin.com/jobs+{query.replace(' ', '+')}"
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for g in soup.find_all('a'):
        href = g.get('href')
        if href and "linkedin.com/jobs" in href:
            clean_link = href.split("&")[0].replace("/url?q=", "")
            links.append(clean_link)
    return list(set(links))[:10]
