# URL of CoinMarketCap
BASE_URL = "https://coinmarketcap.com/"
API_URL = ('https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100'
           '&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all'
           '&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,'
           'tags,platform,max_supply,circulating_supply,total_supply,volume_7d,volume_30d')

# Headers to avoid potential blocking from CoinMarketCap
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# CSV file for storing data
API_CSV_FILE = "top_coins_api.csv"
CSV_FILE = "top_coins.csv"
