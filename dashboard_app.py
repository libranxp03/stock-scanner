import streamlit as st
from database import get_recent_alerts
from scanner import tier2_scan

st.set_page_config(page_title="📊 Stock Intelligence Dashboard", layout="wide")
st.title("📊 Stock Intelligence Dashboard")

alerts = get_recent_alerts()
total_scanned = 0  # Optional: replace with live count
total_trades = 0   # Optional: replace with live count
filtered_alerts = len(alerts)

st.markdown(f"**Assets Scanned:** {total_scanned} | **Trades:** {total_trades} | **Filtered Alerts:** {filtered_alerts}")
st.button("🔍 Run Manual Scan", on_click=lambda: tier2_scan(""))

if not alerts:
    st.warning("No alerts found yet. Waiting for next scan or manual trigger.")
else:
    for alert in alerts:
        with st.expander(f"📈 ${alert['ticker']} | Tier {alert['tier']}"):
            st.markdown(f"**Price:** ${alert['price']}  \n**RSI:** {alert['rsi']}  \n**EMA:** {alert['ema']}  \n**VWAP:** {alert['vwap']}  \n**ATR:** {alert['atr']}")
            st.markdown(f"**Validation:** {alert['narrative']}  \n**Entry:** {alert['entry']}  \n**TP:** {alert['tp']}  \n**SL:** {alert['sl']}")
            st.markdown(f"[Sentiment]({alert['sentiment_link']}) | [Catalyst]({alert['catalyst_link']}) | [News]({alert['news_link']}) | [TradingView](https://www.tradingview.com/symbols/{alert['ticker']}) | [Webull](https://www.webull.com/quote/{alert['ticker']})")
