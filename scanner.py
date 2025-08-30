from database import log_alert
from telegram_bot import send_alert

# 🔧 Dummy test data to verify pipeline
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

if __name__ == "__main__":
    tier1_scan()
