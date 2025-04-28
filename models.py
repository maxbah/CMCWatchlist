from pydantic import BaseModel, root_validator


class Quote(BaseModel):
    name: str
    price: float
    percentChange24h: float
    marketCap: float


class CoinData(BaseModel):
    cmcRank: int
    name: str
    symbol: str
    quotes: list[Quote]


class CoinInfo(BaseModel):
    cmcRank: int
    name: str
    symbol: str
    price: float
    percentChange24h: float
    marketCap: float


class CryptoCurrencyList(BaseModel):
    cryptoCurrencyList: list[CoinData]
