import threading
import time
import requests
import uuid
from urllib.parse import urljoin
from comfy.cli_args import args
import os

base_url = args.express_server_url.rstrip('/') + '/'  # Ensures a single trailing slash
URL = urljoin(base_url, 'backend/heartbeat')

# Hardcoded heartbeat interval (2 seconds)
# HEARTBEAT_INTERVAL = 2  
# Hardcoded heartbeat interval (30 seconds)
HEARTBEAT_INTERVAL = 30  

# Prevent multiple threads from being created if the script is imported multiple times
heartbeat_started = False

BACKEND_TOKEN = os.getenv("BACKEND_TOKEN", "default-secret")  # Load from env

def send_heartbeat():
    headers = {"X-Backend-Token": BACKEND_TOKEN}  # Add authentication header
    while True:
        try:
            payload = {
                "port": args.port,
                "type": "cpu" if args.cpu else "gpu",
            }
            requests.post(URL, json=payload, headers=headers, timeout=1)
        except Exception as e:
            print(f"Heartbeat error: {e}")
        time.sleep(HEARTBEAT_INTERVAL)

# Start the heartbeat thread when imported (but only once)
def start():
    global heartbeat_started
    if heartbeat_started:
        return
    heartbeat_started = True
    heartbeat_thread = threading.Thread(target=send_heartbeat, daemon=True)
    heartbeat_thread.start()
