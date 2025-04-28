import requests

from configs.configuration import *
from parsers.scraper import coin_parser_html, fetch_page
from parsers.parser import extract_coin_info_list
from store_to_csv import store_to_csv
from models import CryptoCurrencyList


def parse_coins():
    """Main function to parse top 100 coins"""
    content = requests.get(API_URL)
    coin_info = extract_coin_info_list(CryptoCurrencyList.parse_obj(content.json()['data']))
    store_to_csv(coin_info, API_CSV_FILE)
    print(f"Parsing completed. {len(coin_info)} coins saved to {API_CSV_FILE}")


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

