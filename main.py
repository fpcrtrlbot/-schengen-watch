import requests
import time
import os
from datetime import datetime

URL = "https://appointment.as-visa.com/tr/istanbul-bireysel-basvuru"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

CHECK_INTERVAL = 300  # 5 dakika

last_state = None


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})


def check_site():
    try:
        r = requests.get(URL, timeout=20)
        html = r.text.lower()

        if "uygun randevu kotası bulunmamaktadır" in html:
            return False

        return True

    except:
        return False


def run():
    global last_state

    send_message("🟢 Schengen Watch başladı (Portekiz)")

    while True:
        status = check_site()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if status and last_state != True:
            send_message(
                f"🚨 PORTekiz RANDEVU BULUNDU!\n\n"
                f"📍 İstanbul\n"
                f"👤 Bireysel Başvuru\n"
                f"🕒 {now}\n\n"
                f"🔗 {URL}"
            )

        last_state = status
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    run()
