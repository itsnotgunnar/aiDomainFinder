# aiDomainFinder
This repository finds the domains of the companies with the highest market caps and checks the '.ai' availability using the GoDaddy API. It uses Python scripts to scrape data, check domain availability, and store the results.

## Table of Contents

    Features
    Requirements
    Installation
    Usage
    Contributing
    License
    Contact

## Features

    Web scraping to gather company information and AI-related terms.
    Checking the availability of domains.
    Exporting available domains to .csv and .txt files.

## Requirements

    Python 3.x
    BeautifulSoup
    Requests
    Godaddy API credentials (for domain availability check)

## Installation

    Clone the repository

    bash

git clone https://github.com/itsnotgunnar/aiDomainFinder.git

## Navigate to the project directory

bash

cd aiDomainFinder

Install required Python packages

pip install -r requirements.txt

## Usage

    Run web_scraper.py to scrape company information.

python web_scraper.py

Run check_availability.py to check domain availability.

    python check_availability.py

    Check the available_domains.txt and ai_converted_domains.csv for results.

## Contributing

Feel free to submit pull requests or open issues to improve the project.
License

This project is open-source, contributions are welcome.
Contact

For any queries, reach out at gunnar@gunnar.ai.
