import csv


def store_to_csv(coin_data, file_name):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ['rank', 'name', 'symbol', 'price_usd',
             'percent_change_24h', 'market_cap_usd'])
        for coin in coin_data:
            writer.writerow([coin.get('rank'),
                             coin.get('name'),
                             coin.get('symbol'),
                             coin.get('price_usd'),
                             coin.get('percent_change_24h'),
                             coin.get('market_cap_usd'),
                             ])
