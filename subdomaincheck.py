import requests
import time
from tabulate import tabulate

class SubdomainChecker:
    def __init__(self, subdomains):
        self.subdomains = subdomains

    def check_status(self):
        results = []
        for subdomain in self.subdomains:
            url = f'http://{subdomain}'
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    status = 'Up'
                else:
                    status = 'Down'
            except requests.ConnectionError:
                status = 'Down'
            results.append([subdomain, status])
        return results

subdomains = ['mail.google.com', 'map.google.com', 'images.google.com']
checker = SubdomainChecker(subdomains)

while True:
    results = checker.check_status()
    headers = ['Subdomain', 'Status']
    print(tabulate(results, headers=headers, tablefmt='grid'))
    time.sleep(60)  # Wait for 60 seconds before checking again
