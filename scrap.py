import csv
import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text()

emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
phone_numbers = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b', text)
addresses = re.findall(r'\d+\s+[\w\s]+\n[\w\s]+,\s+\w+\s+\d+', text)

with open('scraped_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Emails', 'Phone Numbers', 'Addresses'])
    for i in range(max(len(emails), len(phone_numbers), len(addresses))):
        writer.writerow([emails[i] if i < len(emails) else '',
                         phone_numbers[i] if i < len(phone_numbers) else '',
                         addresses[i] if i < len(addresses) else ''])
