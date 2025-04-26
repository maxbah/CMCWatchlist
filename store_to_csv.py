import csv


def store_to_csv(data: list, file_name):
    """Store the scraped data into a CSV file."""
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['rank', 'name', 'symbol', 'price_usd', 'percent_change_24h', 'market_cap_usd']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
