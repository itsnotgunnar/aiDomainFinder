import os
import re
import csv
import json
import requests
from bs4 import BeautifulSoup
from collections import deque

# Constants
BASE_URL = "https://www.value.today/world-top-companies-by-value"
HEADERS = {"User-Agent": "Mozilla/5.0"}
api_key = os.environ.get('GODADDY_API_KEY')
api_secret = os.environ.get('GODADDY_API_SECRET')

def get_attribute(company, selector, attribute=None):
    try:
        if attribute:
            return company.select_one(selector)[attribute]
        else:
            return company.select_one(selector).text.strip()
    except Exception:
        return "Unknown"

def get_company_data():
    all_companies = []
    current_url = BASE_URL
    MAX_PAGES = 2000
    i = 0

    while current_url and i < MAX_PAGES:
        response = requests.get(current_url, headers=HEADERS)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        companies = soup.find_all('div', class_='well node node--type-listed-companies node--view-mode-teaser ds-2col-stacked clearfix')

        for company in companies:
            all_companies.append({
                "rank": get_attribute(company, '.field--name-field-world-rank-dec-25-2022- .field--item'),
                "company_name": get_attribute(company, '.field--name-node-title a'),
                "company_domain": get_attribute(company, '.field--name-field-company-website a', 'href'),
                "company_summary": get_attribute(company, '.field--name-body .field--item'),
                "market_cap": get_attribute(company, '.field--name-field-market-cap-dec-25-2022- .field--item')
            })

        next_page = soup.find('li', class_='pager__item--next').find('a', rel='next')
        if next_page:
            current_url = BASE_URL + next_page['href']
        else:
            current_url = None

        i += 1

    return all_companies

def convert_json_domains():
    with open('companies.json') as f:
        companies = json.load(f)
    
    domains = []
    for company in companies:
        domain = company['company_domain']
        if domain != 'Unknown':
            parsed_domain = re.search('https?://([A-Za-z_0-9.-]+).*', domain)
            if parsed_domain:
                domain_name = parsed_domain.group(1).split('.')
                domain_name = domain_name[1] if 'www' in domain_name[0] else domain_name[0]
                domains.append(f"{domain_name}.ai")
    return domains

def check_domain_availability(domains):
    available_domains = []
    for domain in domains:
        endpoint = f"https://api.godaddy.com/v1/domains/available?domain={domain}"
        headers = {"Authorization": f"sso-key {api_key}:{api_secret}", "Accept": "application/json"}

        response = requests.get(endpoint, headers=headers)
        data = response.json()

        if data.get("available", False):
            available_domains.append(domain)
            print(f"{domain} is available.")
        else:
            print(f"{domain} is not available.")
    return available_domains

if __name__ == "__main__":
    company_data = get_company_data()
    with open('companies.json', 'w') as f:
        json.dump(company_data, f, indent=4)

    domains_to_check = convert_json_domains()
    available_domains = check_domain_availability(domains_to_check)
    
    # Saving available domains to a file
    with open('available_domains.txt', 'w') as f:
        for domain in available_domains:
            f.write(f"{domain}\n")