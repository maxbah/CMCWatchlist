def coin_parser_api(content: dict):
    """API result parser """
    coins = []
    for item in content['data']['cryptoCurrencyList']:
        rank = item['cmcRank']
        name = item['name']
        symbol = item['symbol']
        for j in item['quotes']:
            if j['name'] == 'USD':
                price = j['price']
                percent_change_24 = j['percentChange24h']
                market_cap = j['marketCap']
                coins.append({
                    "rank": rank,
                    "name": name,
                    "symbol": symbol,
                    "price_usd": price,
                    "percent_change_24h": percent_change_24,
                    "market_cap_usd": market_cap})
    return coins
