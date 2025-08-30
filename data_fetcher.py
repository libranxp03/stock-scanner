from api_clients import get_ohlcv, get_rsi, get_ema, get_vwap, get_news_link, get_sentiment_link

def fetch_tickers():
    # Replace with live API call to your stock universe
    return []  # Empty by default; scanner skips if no tickers

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
