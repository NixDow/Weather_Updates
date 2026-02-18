import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("tel_bot_tkn")
CHAT_ID = os.getenv("tel_chat")

def telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Error sending message:", e)
