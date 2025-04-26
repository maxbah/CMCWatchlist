
# CoinMarketCap Watchlist

A Python script for collecting information about the top 100 cryptocurrencies 
from [CoinMarketCap](https://coinmarketcap.com/) saving the data to a CSV file. 

---

## Developed by

Bakhovskyi Maksym - python software developer

---

## Requirements

- Python 3.9+
- Internet connection (for live API calls)

---

##  Features 

- Parses top 10 from the CoinMarketCap website. 
- Extracts the following data for each coin: 
  - Rank (`rank`) 
  - Name (`name`) 
  - Symbol (`symbol`) 
  - Price in USD (`price_usd`) 
  - 24h percentage change (`percent_change_24h`) 
  - Market capitalization in USD (`market_cap_usd`) 
- Saves the results to a CSV file.

---

##  Installation 1

1.Clone the repository:
```bash
git clone https://github.com/maxbah/CMCWatchlist.git
cd CMCWatchlist
 ```

2.Install the dependencies: 

```bash 
pip install -r requirements.txt 
``` 

Or install manually: 

```bash 
pip install requests beautifulsoup4 
``` 

---

## Usage Simply run the script: 

```bash 
python main.py 
``` 

After execution, a CSV file will be created with 100 coins
and their details. 

---

## Sample Output 
```
csv rank,name,symbol,price_usd,percent_change_24h,market_cap_usd 
1,Bitcoin,BTC,64873.44,0.85,1265478230000 2,Ethereum,ETH,3185.42,-1.52,382145000000 ... 
``` 

---

## Notes

The HTML structure on CoinMarketCap may change. 
If the layout is updated, the code may work incorrect
