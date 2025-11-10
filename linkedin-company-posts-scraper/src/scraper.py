thonimport requests
from .extractors.linkedin_parser import parse_linkedin_page
from .outputs.data_exporter import export_data
import json

class LinkedInScraper:
    def __init__(self, company_name):
        self.company_name = company_name
        self.base_url = f"https://www.linkedin.com/company/{company_name}/posts/"
        self.posts = []

    def fetch_posts(self, page_number=1):
        url = f"{self.base_url}?page={page_number}"
        response = requests.get(url)
        if response.status_code == 200:
            posts_data = parse_linkedin_page(response.text)
            self.posts.extend(posts_data)
            return True
        return False

    def scrape(self, max_pages=10):
        page_number = 1
        while page_number <= max_pages:
            if not self.fetch_posts(page_number):
                break
            page_number += 1
        return self.posts

    def save_data(self, filename="output.json"):
        with open(filename, 'w') as f:
            json.dump(self.posts, f, indent=4)

if __name__ == "__main__":
    scraper = LinkedInScraper("google")
    data = scraper.scrape()
    scraper.save_data()