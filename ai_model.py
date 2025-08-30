def run_model(data):
    score = 0
    if data['rsi'] < 30: score += 2
    if data['rvol'] > 1.5: score += 2
    if data['price_change'] > 2: score += 2
    if data['ema_stack'] == 'bullish': score += 2
    if abs(data['vwap_proximity']) < 1: score += 2

    narrative = "High momentum breakout with strong volume and bullish EMA stack."
    risk = {
        "entry": "Breakout above VWAP",
        "tp": "10-15% above entry",
        "sl": "Below EMA or ATR"
    }
    return score, narrative, risk
