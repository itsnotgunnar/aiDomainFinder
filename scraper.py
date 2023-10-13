import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.value.today/world-top-companies-by-value"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_attribute(company, selector, attribute=None):
    try:
        if attribute:
            return company.select_one(selector)[attribute]
        else:
            return company.select_one(selector).text.strip()
    except:
        return "Unknown"

def get_company_data():
    current_url = BASE_URL
    all_companies = []
    MAX_PAGES = 2000
    i = 0

    while current_url and i < MAX_PAGES:
        response = requests.get(current_url, headers=HEADERS)
        
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        companies = soup.find_all('div', class_='well node node--type-listed-companies node--view-mode-teaser ds-2col-stacked clearfix')

        for company in companies:
            rank = get_attribute(company, '.field--name-field-world-rank-dec-25-2022- .field--item')
            name = get_attribute(company, '.field--name-node-title a')
            domain = get_attribute(company, '.field--name-field-company-website a', 'href')
            summary = get_attribute(company, '.field--name-body .field--item')
            market_cap = get_attribute(company, '.field--name-field-market-cap-dec-25-2022- .field--item')

            all_companies.append({
                "rank": rank,
                "company_name": name,
                "company_domain": domain,
                "company_summary": summary,
                "market_cap": market_cap
            })

        # Check for the next page link
        next_page = soup.find('li', class_='pager__item--next').find('a', rel='next')
        if next_page:
            current_url = BASE_URL + next_page['href']
        else:
            current_url = None

        i += 1
        
    return all_companies

if __name__ == "__main__":
    data = get_company_data()
    with open('top_companies.json', 'w') as f:
        json.dump(data, f, indent=4)
