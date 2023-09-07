import csv, json
# import regular expressions for replacing the current domain with the .ai version
import re
from sympy import true, false
import requests
from bs4 import BeautifulSoup


def convert_domains():
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
        url = BASE_URL + domain
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        available = soup.find('div', class_='ms0 mb-0')
        if available:
            print(domain + ' is available')
        else:
            print(domain + ' is not available')

def find_available(domains):
    """Check if a domain is available for purchase"""
    # Filter out the available domains
    available_domains = [d for d in domains if d['available']]

    # Write the available domains to a CSV file
    with open('available_domains.csv', 'w', newline='') as csvfile:
        fieldnames = ['domain', 'available', 'purchaseLink']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for domain in available_domains:
            writer.writerow(domain)

def write_to_txt(domains):
    """Write the domains to a txt file"""
    print(domains)
    with open('ai_domains.txt', 'w') as f:
        for domain in domains:
            f.write(f"{domain} , ")

def main():
    domains = convert_domains()
    check_avaliability(domains)
    write_to_txt(domains)
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
https://www.chinaunicom.com.hk
https://www.schindler.com
https://www.cicc.com/
https://www.adaniports.com/
https://www.molinahealthcare.com
https://www.pttep.com/
http://www.zhifeishengwu.com/
https://www.berkley.com/
https://www.bb.com.br
https://www.crrcgc.cc
https://www.longfor.com/en/
https://www.ntpc.co.in/
https://www.fortisinc.com/
https://www.pbebank.com/
https://www.biomarin.com/
https://eletrobras.com
http://www.tpltrust.com/
https://www.centerpointenergy.com
https://zoom.us/
https://carlsberggroup.com/
https://www.wilmar-international.com/
http://www.weston.ca/
https://www.viacom.com/
https://www.invitationhomes.com/
https://www.rollins.com/
https://www.essity.com/
https://www.wabtec.com/
https://corporate.m3.com/
Unknown
Unknown
https://www.legalandgeneral.com/
https://www.kakaocorp.com/?lang=en
https://www.ventasreit.com/
https://www.dukerealty.com/
https://www.steris.com/
https://www.wheatonpm.com/
https://www.npc.com.tw
https://www.jasolar.com.cn/
https://www.incyte.com/
http://www.mengniuir.com
https://www.aeon.info/en/
https://www.maac.com/
http://www.baosteel.com
https://www.otsuka.com/en/
https://www.steeldynamics.com/
https://www.bestbuy.com/
https://www.clpgroup.com/en
http://www.fpcusa.com/
https://www.gulf.co.th/en/
https://www.amcor.com/
https://www.cathayholdings.com
http://www.wens.com.cn/
`.
for example, https://www.clpgroup.com/en would be clpgroup.ai. put all of these domains in a list. 'U
nknown' should not be added to the list
'''