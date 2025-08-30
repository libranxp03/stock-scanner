from database import log_alert
from telegram_bot import send_alert

# 🔧 Dummy Tier 1 scan for testing
def tier1_scan():
    ticker = "AAPL"
    data = {
        "price": 192.34,
        "price_change": 2.1,
        "volume": 3_500_000,
        "rsi": 61,
        "rvol": 1.5,
        "ema_stack": "bullish",
        "vwap_proximity": 0.8,
        "atr": 2.3,
        "is_pump": False
    }
    send_alert(ticker, data, tier=1)
    log_alert(ticker, tier=1)

# ✅ Minimal Tier 2 scan to satisfy dashboard import
def tier2_scan(ticker):
    data = {
        "price": 192.34,
        "price_change": 2.1,
        "volume": 3_500_000,
        "rsi": 61,
        "rvol": 1.5,
        "ema_stack": "bullish",
        "vwap_proximity": 0.8,
        "atr": 2.3,
        "entry": 191.5,
        "tp": 195.0,
        "sl": 189.0,
        "score": 8,
        "narrative": "Strong volume surge with bullish EMA stack.",
        "sentiment_link": "https://finnhub.io/news/AAPL",
        "catalyst_link": "https://newsapi.org/catalyst/AAPL",
        "news_link": "https://newsapi.org/news/AAPL"
    }
    send_alert(ticker, data, tier=2)
    log_alert(ticker, tier=2, score=data["score"])

if __name__ == "__main__":
    tier1_scan()
