import csv, json
import re
from sympy import true, false
import requests
from bs4 import BeautifulSoup
import os
import godaddypy
# import lib that allows me to dequque from a list
from collections import deque

api_key = godaddypy.api_key = os.environ.get('GODADDY_API_KEY')
api_secret = godaddypy.api_secret = os.environ.get('GODADDY_API_SECRET')

# api_key = os.environ.get('GODADDY_API_KEY')
# api_secret = os.environ.get('GODADDY_API_SECRET')


available_domains = []
checked_domains = []

def convert_json_domains():
    with open('top_companies.json') as f:
        companies = json.load(f)

    domains = []
    for company in companies:
        domain = company['company_domain']

        if domain != 'Unknown':
            domain = re.search('https?://([A-Za-z_0-9.-]+).*', domain)
            if domain:
                domain_name = domain.group(1)
                domain_name = domain_name.split('.')
                domain_name = domain_name[1] if 'www' in domain_name[0] else domain_name[0]
                domains.append(domain_name + '.ai')
            print(domain_name + '.ai')
    return domains

def check_avaliability(domains):
    BASE_URL = 'https://oneword.domains/d/'
    for domain in domains:
        url = f"https://www.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={domain}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find('div', {'class': 'search-results px-0'})

    if result:
        print(domain + ' is available')
        available_domains.append(domain)
    else:
        print(f"{domain} is not available")

def txt_to_list():
    """Convert a CSV file to a list of strings"""
    with open('unchecked_domains.txt', 'r') as f:
        domains = f.read()[:-1].split(',')
        domains.pop()
        return domains

def check_domain_availability(domains):
    """Check if a domain is available for purchase"""
    for domain in domains:
        # GoDaddy API endpoint for checking domain availability
        endpoint = f"https://api.godaddy.com/v1/domains/available?domain={domain}"

        headers = {
            "Authorization": f"sso-key {api_key}:{api_secret}",
            "Accept": "application/json"
        }

        try:
            response = requests.get(endpoint, headers=headers)
            data = response.json()
        
            if data["available"]:
                available_domains.append(domain)
                print(f"The domain {domain} is available on GoDaddy!")
                checked_domains.append(domain)
                domains = domains.remove(domain)
            else:
                print(f"The domain {domain} is not available on GoDaddy.")
                checked_domains.append(domain)
                domains = domains.remove(domain)


        except Exception as e:
            print(e)
            write_to_txt(checked_domains,'checked_domains.txt', 'a')
            write_to_txt(domains,'unchecked_domains.txt', 'w')
            exit()



    
def find_available(domains):
    """Check if a domain is available for purchase"""
    # Filter out the available domains
    available_domains = [d for d in domains if d['available']]

    # Write the available domains to a CSV file
    with open('sten', 'a', newline='') as csvfile:
        fieldnames = ['domain', 'available', 'purchaseLink']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for domain in available_domains:
            writer.writerow(domain)

def write_to_txt(domains, filename, mode):
    """Write the domains to a txt file"""
    with open(filename, mode=mode) as f:
        for domain in domains:
          f.write(domain + ',')

domains = convert_json_domains()
write_to_txt(domains, 'available_domains.txt', 'w')
exit()

def main():
    if os.path.exists('unchecked_domains.txt'):
        domains = txt_to_list()
    else:
        domains = convert_json_domains()
    check_domain_availability(domains)
    # find_available(domains)

if __name__ == '__main__':
    main()
    
'''
ai_domains = []

for url in urls:
    if url != 'Unknown':
        domain = re.search('https?://([A-Za-z_0-9.-]+).*', url)
        if domain:
            domain_name = domain.group(1)
            domain_name = domain_name.split('.')
            domain_name = domain_name[1] if 'www' in domain_name[0] else domain_name[0]
            ai_domains.append(domain_name + '.ai')

print(ai_domains)

create a regex in python that will replace domain names with their '.ai' version. here are some samples:'
'''