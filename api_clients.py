import os
import requests

POLYGON_KEY = os.environ.get("POLYGON_KEY")
FMP_KEY = os.environ.get("FMP_KEY")
ALPHA_KEY = os.environ.get("ALPHA_KEY")
FINNHUB_KEY = os.environ.get("FINNHUB_KEY")
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")

def get_ohlcv(ticker):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={POLYGON_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['results'][0] if 'results' in data else None
    except: return None

def get_rsi(ticker):
    url = f"https://financialmodelingprep.com/api/v3/technical_indicator/{ticker}?type=rsi&period=14&apikey={FMP_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data[0]['rsi'] if data else None
    except: return None

def get_ema(ticker):
    url = f"https://financialmodelingprep.com/api/v3/technical_indicator/{ticker}?type=ema&period=20&apikey={FMP_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data[0]['ema'] if data else None
    except: return None

def get_vwap(ticker):
    url = f"https://api.polygon.io/v1/indicators/vwap/{ticker}?timespan=day&apiKey={POLYGON_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['vwap'] if 'vwap' in data else None
    except: return None

def get_news_link(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&apiKey={NEWSAPI_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["articles"][0]["url"] if data.get("articles") else None
    except: return None

def get_sentiment_link(ticker):
    url = f"https://finnhub.io/api/v1/news-sentiment?symbol={ticker}&token={FINNHUB_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("url") or f"https://finnhub.io/news/{ticker}"
    except: return None
