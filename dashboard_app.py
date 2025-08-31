import streamlit as st
from database import get_recent_alerts
from scanner import tier2_scan

st.set_page_config(page_title="📊 Stock Intelligence Dashboard", layout="wide")
st.title("📊 Stock Intelligence Dashboard")

# 🔄 Load alerts from Supabase
alerts = get_recent_alerts()

# 📊 Display scan metrics
total_scanned = 128  # Replace with live count if available
filtered_alerts = len(alerts)
alert_rate = round((filtered_alerts / total_scanned) * 100, 2) if total_scanned else 0

st.markdown(f"""
<div style="display: flex; gap: 2rem;">
    <div><strong>Assets Scanned:</strong> {total_scanned}</div>
    <div><strong>Filtered Alerts:</strong> {filtered_alerts} ({alert_rate}%)</div>
</div>
""", unsafe_allow_html=True)

# 🔘 Manual scan trigger
if st.button("🔍 Run Manual Scan"):
    tier2_scan()

# 📈 Display alert cards
if not alerts:
    st.warning("No alerts found yet. Waiting for next scan or manual trigger.")
else:
    for alert in alerts:
        st.markdown("---")
        st.subheader(f"📈 ${alert['ticker']} | Tier {alert['tier']}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("RSI", alert['rsi'])
            st.metric("EMA", alert['ema'])
        with col2:
            st.metric("VWAP", alert['vwap'])
            st.metric("ATR", alert['atr'])
        with col3:
            st.metric("Price", alert['price'])
            st.metric("Change", f"{alert['price_change']}%")

        st.markdown(f"**Validation Entry:** {alert['narrative']}")
        st.markdown(f"**Validation Strength:** High momentum breakout")
        st.markdown(f"**TP (Take Profit):** {alert['tp']}")
        st.markdown(f"**SL (Stop Loss):** {alert['sl']}")

        st.markdown(f"""
        🔗 [Trending]({alert['sentiment_link']})  
        🔗 [Catalyst]({alert['catalyst_link']})  
        🔗 [News]({alert['news_link']})  
        🔗 [Twitter](https://twitter.com/search?q={alert['ticker']})  
        🔗 [Reddit](https://www.reddit.com/search/?q={alert['ticker']})
        """)
