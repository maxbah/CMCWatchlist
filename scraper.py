import requests
from bs4 import BeautifulSoup

from configs.configuration import HEADERS


def fetch_page(url: str):
    """Fetch the content of a given URL."""
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve {url}")
        return None


def coin_parser_html(html_content: str):
    """Parse the HTML content of a page and extract relevant data."""
    soup = BeautifulSoup(html_content, "lxml")
    table = soup.find('table', {'class': 'cmc-table'})
    rows = table.find_all('tr')
    coins = []
    for row in rows:
        cols = row.find_all('td')
        if len(cols) <= 7:
            continue
        rank = cols[1].find('p', {'class': 'sc-71024e3e-0 jBOvmG'}).text
        name = cols[2].find('p', {'class': 'sc-65e7f566-0 iPbTJf coin-item-name'}).text
        symbol = cols[2].find('p', {'class': 'sc-65e7f566-0 byYAWx coin-item-symbol'}).text
        price = cols[3].text.strip().replace('$', '').replace(',', '')
        percent_change = cols[4].text.strip().replace('%', '')
        market_cap = cols[7].find('span', {'class': 'sc-11478e5d-1 jfwGHx'}).text.replace('$', '')
        coins.append({
            "rank": rank,
            "name": name,
            "symbol": symbol,
            "price_usd": price,
            "percent_change_24h": percent_change,
            "market_cap_usd": market_cap
        })
    return coins
