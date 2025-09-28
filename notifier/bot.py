import requests
from bs4 import BeautifulSoup

# === 配置 ===
DOMAINS = {
    "Hax": "https://hax.co.id/create-vps",
    "Woiden": "https://woiden.id/create-vps"
}

BOT_TOKEN = "example"   # ← 替换为你的 Telegram Bot Token
CHAT_ID = "example"      # ← 替换为你的频道或用户 ID
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
TIMEOUT = 10

# === 抓取并解析 select#datacenter 的有效选项 ===
def fetch_available(name, url):
    try:
        html = requests.get(url, headers=HEADERS, timeout=TIMEOUT).text
        soup = BeautifulSoup(html, "html.parser")
        select = soup.find("select", id="datacenter")
        if not select:
            return []

        options = select.find_all("option")
        valid = []
        for opt in options:
            text = opt.get_text(strip=True)
            value = (opt.get("value") or "").strip()
            if text != "-select-" and value:
                valid.append(text)
        return valid
    except Exception as e:
        print(f"[ERROR] {name} fetch failed: {e}")
        return []

# === Telegram 推送 ===
def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": msg}
    try:
        requests.post(url, json=payload, timeout=TIMEOUT)
    except Exception as e:
        print(f"[ERROR] Telegram failed: {e}")

# === 主流程 ===
def main():
    lines = []
    for name, url in DOMAINS.items():
        available = fetch_available(name, url)
        for dc in available:
            lines.append(f"- {name}: {dc}")

if lines:
    msg = "✅ 有VPS\n" + "\n".join(lines)
    send_telegram(msg)
else:
    print("[INFO] 无VPS，不发送消息")

if __name__ == "__main__":
    main()
