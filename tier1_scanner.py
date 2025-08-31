from data_fetcher import fetch_tickers, fetch_indicators
from telegram_bot import send_alert
from database import log_alert, check_recent_alerts

def is_valid(data):
    required = ['price', 'price_change', 'volume', 'rsi', 'rvol', 'ema', 'vwap', 'vwap_proximity', 'ema_stack', 'atr']
    return data and all(data.get(k) is not None for k in required)

def run_tier1_scan():
    tickers = fetch_tickers()
    for ticker in tickers:
        if check_recent_alerts(ticker): continue
        data = fetch_indicators(ticker)
        if not is_valid(data): continue
        if (
            data['price_change'] > 1 and
            data['rvol'] > 1.2 and
            45 <= data['rsi'] <= 75 and
            data['ema_stack'] == 'bullish' and
            abs(data['vwap_proximity']) <= 1.5
        ):
            send_alert(ticker, data, tier=1)
            log_alert(ticker, tier=1)

if __name__ == "__main__":
    run_tier1_scan()
