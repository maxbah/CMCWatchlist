from models import CryptoCurrencyList


def extract_coin_info_list(crypto_data: CryptoCurrencyList) -> list[dict[str, str | float | int]]:
    coin_info_dicts = []
    for coin in crypto_data.cryptoCurrencyList:
        usd_quote = next((quote for quote in coin.quotes if quote.name == 'USD'), None)
        if usd_quote:
            coin_info_dicts.append({
                'rank': coin.cmcRank,
                'name': coin.name,
                'symbol': coin.symbol,
                'price_usd': usd_quote.price,
                'percent_change_24h': usd_quote.percentChange24h,
                'market_cap_usd': usd_quote.marketCap}
            )
    return coin_info_dicts
