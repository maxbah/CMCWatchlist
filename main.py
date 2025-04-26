import requests

from configs.configuration import *
from parsers.scraper import coin_parser_html, fetch_page
from parsers.parser import coin_parser_api
from store_to_csv import store_to_csv


def parse_coins():
    """Main function to parse top 100 coins"""
    content = requests.get(API_URL)
    res = coin_parser_api(content.json())
    store_to_csv(res, API_CSV_FILE)
    print(f"Parsing completed. {len(res)} coins saved to {API_CSV_FILE}")


def scrape_coins():
    """Main function to scrape top 100 coins"""
    url = f"{BASE_URL}?page=1"
    html_content = fetch_page(url)
    coins_on_page = coin_parser_html(html_content)
    store_to_csv(coins_on_page, CSV_FILE)
    print(f"Scraping completed. {len(coins_on_page)} coins saved to {CSV_FILE}")


if __name__ == "__main__":
    scrape_coins()
    parse_coins()

