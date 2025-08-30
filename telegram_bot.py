from telegram import Bot
import os

bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_alert(ticker, data, tier=1):
    msg = f"🚨 *${ticker}* | Price: ${data['price']} | Change: {data['price_change']}% | Volume: {data['volume']}"
    bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode="Markdown")
    print(f"✅ Telegram alert sent for {ticker}")
