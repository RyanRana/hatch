import requests, re
from bs4 import BeautifulSoup
import json

def scrape_jobs(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={query}+site:linkedin.com/jobs+OR+site:indeed.com+OR+site:remoteok.com"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    results = []
    for link in soup.find_all('a', href=True):
        if 'http' in link['href']:
            title = link.get_text().strip()
            match = re.search(r"url\?q=(.*?)&", link['href'])
            if match:
                results.append({"title": title, "url": match.group(1), "description": title})

    with open("jobs.json", "w") as f:
        json.dump(results, f)

    return results
