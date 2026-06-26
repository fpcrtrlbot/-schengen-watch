import requests
import os
from datetime import datetime

URL = "https://appointment.as-visa.com/tr/istanbul-bireysel-basvuru"

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})


def check_site():
    try:
        r = requests.get(URL, timeout=20)
        html = r.text.lower()

        # kapalı ifade
        if "uygun randevu kotası bulunmamaktadır" in html:
            return False

        return True

    except:
        return None


def run():
    status = check_site()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if status is True:
        msg = f"🟢 Kontrol: {now}\n📍 Portekiz randevu AÇIK olabilir!"
    elif status is False:
        msg = f"🔴 Kontrol: {now}\n📍 Randevu kapalı"
    else:
        msg = f"⚠️ Kontrol: {now}\n📍 Siteye erişilemedi"

    send_message(msg)


if __name__ == "__main__":
    run()
