import requests
import os
from api_clients import get_ohlcv, get_rsi, get_ema, get_vwap, get_news_link, get_sentiment_link

# 🔐 Load all API keys securely
POLYGON_KEY = os.environ.get("POLYGON_KEY")
FMP_KEY = os.environ.get("FMP_KEY")
ALPHA_KEY = os.environ.get("ALPHA_KEY")
FINNHUB_KEY = os.environ.get("FINNHUB_KEY")
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")
REDDIT_KEY = os.environ.get("REDDIT_KEY")
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")

def fetch_tickers():
    url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&limit=1000&apiKey={POLYGON_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return [t['ticker'] for t in data['results'] if t['primary_exchange'] in ['XNAS', 'XNYS']]
    except Exception as e:
        print(f"❌ Failed to fetch tickers: {e}")
        return []

def fetch_indicators(ticker):
    ohlcv = get_ohlcv(ticker)
    if not ohlcv: return None

    ema = get_ema(ticker)
    vwap = get_vwap(ticker)

    return {
        "price": ohlcv['c'],
        "price_change": round((ohlcv['c'] - ohlcv['o']) / ohlcv['o'] * 100, 2),
        "volume": ohlcv['v'],
        "rsi": get_rsi(ticker),
        "rvol": ohlcv['v'] / ohlcv['v'],  # Replace with actual RVOL logic
        "ema": ema,
        "vwap": vwap,
        "vwap_proximity": round((ohlcv['c'] - vwap) / vwap * 100, 2) if vwap else None,
        "ema_stack": "bullish" if ohlcv['c'] > ema else "bearish",
        "atr": 2.5  # Replace with actual ATR logic
    }

def fetch_sentiment(ticker):
    return {"sentiment_link": get_sentiment_link(ticker)}

def fetch_news(ticker):
    return {"news_link": get_news_link(ticker)}

def fetch_insider(ticker):
    return {"catalyst_link": get_news_link(ticker)}
