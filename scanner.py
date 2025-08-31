from data_fetcher import fetch_tickers, fetch_indicators, fetch_sentiment, fetch_news, fetch_insider
from telegram_bot import send_alert
from database import log_alert, check_recent_alerts
from ai_model import run_model

def is_valid(data):
    required = ['price', 'price_change', 'volume', 'rsi', 'rvol', 'ema', 'vwap', 'vwap_proximity', 'ema_stack', 'atr']
    return data and all(data.get(k) is not None for k in required)

def tier1_scan():
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

def tier2_scan(ticker=None):
    tickers = [ticker] if ticker else fetch_tickers()
    for t in tickers:
        if check_recent_alerts(t): continue
        data = fetch_indicators(t)
        if not is_valid(data): continue
        sentiment = fetch_sentiment(t)
        news = fetch_news(t)
        insider = fetch_insider(t)
        enriched = {**data, **sentiment, **news, **insider}
        score, narrative, risk = run_model(enriched)
        enriched.update({'score': score, 'narrative': narrative, **risk})
        send_alert(t, enriched, tier=2)
        log_alert(t, tier=2, score=score)

if __name__ == "__main__":
    tier1_scan()
