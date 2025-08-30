import os
import requests

# ✅ Load API keys securely from environment variables
POLYGON_KEY = os.environ.get("POLYGON_KEY")
FMP_KEY = os.environ.get("FMP_KEY")

# 🔍 OHLCV data from Polygon
def get_ohlcv(ticker):
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={POLYGON_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['results'][0] if 'results' in data else None
    except Exception as e:
        print(f"❌ OHLCV fetch failed for {ticker}: {e}")
        return None

# 🔍 Volume data from Polygon
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
