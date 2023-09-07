# Filter out the available domains
available_domains = [d for d in domains if d['available']]

# Write the available domains to a CSV file
with open('available_domains.csv', 'w', newline='') as csvfile:
    fieldnames = ['domain', 'available', 'purchaseLink']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for domain in available_domains:
        writer.writerow(domain)

