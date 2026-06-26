import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("TEST BAŞLADI")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "🧪 TELEGRAM TEST MESAJI"
})

print(r.status_code)
print(r.text)
