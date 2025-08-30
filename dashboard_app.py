import streamlit as st
import os
os.environ["STREAMLIT_SERVER_PORT"] = os.environ.get("PORT", "8501")

from scanner import tier1_scan
from database import get_recent_alerts

st.set_page_config(page_title="📊 Stock Momentum Scanner", layout="wide")
st.title("📊 Stock Momentum Scanner")
st.write("Last Scan: [auto every 45 min]")

alerts = get_recent_alerts()
if not alerts:
    st.warning("No alerts found yet. Waiting for next scan or manual trigger.")
else:
    for alert in alerts:
        with st.expander(f"${alert['ticker']} | Tier {alert['tier']}"):
            st.write(f"Price: ${alert['price']} | Change: {alert['price_change']}% | Volume: {alert['volume']}")
            st.write(f"RSI: {alert['rsi']} | RVOL: {alert['rvol']} | EMA Stack: {alert['ema_stack']} | VWAP Δ: {alert['vwap_proximity']}%")
            st.write(f"ATR: {alert['atr']}")
