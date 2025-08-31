from data_fetcher import fetch_tickers, fetch_indicators, fetch_sentiment, fetch_news, fetch_insider
from telegram_bot import send_alert
from database import log_alert, check_recent_alerts
from ai_model import run_model

def is_valid(data):
    required = ['price', 'price_change', 'volume', 'rsi', 'rvol', 'ema', 'vwap', 'vwap_proximity', 'ema_stack', 'atr']
    return data and all(data.get(k) is not None for k in required)

def run_tier2_scan():
    tickers = fetch_tickers()
    for ticker in tickers:
        if check_recent_alerts(ticker): continue
        data = fetch_indicators(ticker)
        if not is_valid(data): continue
        sentiment = fetch_sentiment(ticker)
        news = fetch_news(ticker)
        insider = fetch_insider(ticker)
        enriched = {**data, **sentiment, **news, **insider}
        score, narrative, risk = run_model(enriched)
        enriched.update({'score': score, 'narrative': narrative, **risk})
        send_alert(ticker, enriched, tier=2)
        log_alert(ticker, tier=2, score=score)

if __name__ == "__main__":
    run_tier2_scan()
