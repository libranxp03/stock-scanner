def run_model(data):
    score = 0
    if data['rsi'] < 30: score += 2
    if data['rvol'] > 1.5: score += 2
    if data['price_change']
