import os
import requests

# ✅ Load API keys securely from environment variables
POLYGON_KEY = os.environ.get("POLYGON_KEY")
FMP_KEY = os.environ.get("FMP_KEY")
ALPHA_KEY = os.environ.get("ALPHA_KEY")
FINNHUB_KEY = os.environ.get("FINNHUB_KEY")
NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY")

# 🔍 OHLCV from Polygon
def get_ohlcv(ticker):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={POLYGON_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['results'][0] if 'results' in data else None
    except Exception as e:
        print(f"❌ OHLCV fetch failed for {ticker}: {e}")
        return None

# 🔍 Volume from Polygon
def get_volume(ticker):
    data = get_ohlcv(ticker)
    return data['v'] if data else None

# 📈 RSI from FMP
def get_rsi(ticker):
    url = f"https://financialmodelingprep.com/api/v3/technical_indicator/{ticker}?type=rsi&period=14&apikey={FMP_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data[0]['rsi'] if data else None
    except Exception as e:
        print(f"❌ RSI fetch failed for {ticker}: {e}")
        return None

# 📈 EMA from FMP
def get_ema(ticker):
    url = f"https://financialmodelingprep.com/api/v3/technical_indicator/{ticker}?type=ema&period=20&apikey={FMP_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data[0]['ema'] if data else None
    except Exception as e:
        print(f"❌ EMA fetch failed for {ticker}: {e}")
        return None

# 📈 VWAP from Polygon
def get_vwap(ticker):
    url = f"https://api.polygon.io/v1/indicators/vwap/{ticker}?timespan=day&apiKey={POLYGON_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['vwap'] if 'vwap' in data else None
    except Exception as e:
        print(f"❌ VWAP fetch failed for {ticker}: {e}")
        return None

# 📈 ATR from Alpha Vantage
def get_atr(ticker):
    url = f"https://www.alphavantage.co/query?function=ATR&symbol={ticker}&interval=daily&time_period=14&apikey={ALPHA_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        series = data.get("Technical Analysis: ATR", {})
        latest = next(iter(series.values()), {})
        return float(latest.get("ATR")) if latest else None
    except Exception as e:
        print(f"❌ ATR fetch failed for {ticker}: {e}")
        return None

# 📰 News from NewsAPI
def get_news_link(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&apiKey={NEWSAPI_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("articles"):
            return data["articles"][0]["url"]
    except Exception as e:
        print(f"❌ News fetch failed for {ticker}: {e}")
    return None

# 🧠 Sentiment from Finnhub
def get_sentiment_link(ticker):
    url = f"https://finnhub.io/api/v1/news-sentiment?symbol={ticker}&token={FINNHUB_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("url") or f"https://finnhub.io/news/{ticker}"
    except Exception as e:
        print(f"❌ Sentiment fetch failed for {ticker}: {e}")
        return None
