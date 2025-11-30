import threading
import time
import requests
from datetime import datetime

# --- Logic Configuration ---
def run_bot(name, url, delay):
    while True:
        start = time.time()
        try:
            # JS had 10s timeout
            res = requests.get(url, timeout=10)
            
            took = time.time() - start
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] [{name}] {url} -> {res.status_code} ({took:.2f}s)")
            
        except Exception as e:
            took = time.time() - start
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # In python Exception messages might be long, keeping it simple
            print(f"[{timestamp}] [{name}] Error: {e} ({took:.2f}s)")

        # JS: await sleep(delay * 1000) -> Python sleep takes seconds
        time.sleep(delay)

# --- URL Groups ---
urls_3sec = [
    "https://siyamahmmed.shop/4sec1.php",
    "https://siyamahmmed.shop/4sec2.php",
    "https://siyamahmmed.shop/4sec3.php",
    "https://siyamahmmed.shop/4sec4.php",
    "https://siyamahmmed.shop/4sec5.php",
    "https://siyamahmmed.shop/4sec6.php",
    "https://siyamahmmed.shop/4sec7.php",
    "https://siyamahmmed.shop/4sec8.php",
    "https://zihadbd.shop/clientbot21.php",
]

special_bots = [
    {"name": "jimkar bot", "url": "https://siyamahmmed.shop/jimkarr.php", "delay": 3},
    {"name": "talhannc bot", "url": "https://zihadbd.shop/talhannc.php", "delay": 2},
]

# --- Execution ---
if __name__ == "__main__":
    # Start 3-sec bots
    for i, url in enumerate(urls_3sec):
        name = f"bot{i + 1}"
        t = threading.Thread(target=run_bot, args=(name, url, 3))
        t.daemon = True
        t.start()

    # Start special bots
    for bot in special_bots:
        t = threading.Thread(target=run_bot, args=(bot["name"], bot["url"], bot["delay"]))
        t.daemon = True
        t.start()

    # Keep process alive
    while True:
        time.sleep(60)
