import requests
import time
from datetime import datetime
from loguru import logger
import os

API_KEY = os.getenv("SERVICE1_API_KEY")
SERVICE_NAME = "Service1"
BASE_URL = "http://localhost:8000"

logger.add(f"{SERVICE_NAME}.log", rotation="100 MB")

def generate_log():
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    messages = [
        "User logged in",
        "Database connection failed",
        "Processing data",
        "Task completed successfully"
    ]
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "service_name": SERVICE_NAME,
        "log_level": logger.level(log_levels[int(time.time()) % len(log_levels)]).name,
        "message": messages[int(time.time()) % len(messages)]
    }

def send_log(log_data):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    try:
        response = requests.post(f"{BASE_URL}/logs", json=log_data, headers=headers)
        response.raise_for_status()
        logger.info(f"Log sent successfully: {log_data}")
    except requests.RequestException as e:
        logger.error(f"Failed to send log: {e}")

if __name__ == "__main__":
    while True:
        log = generate_log()
        send_log(log)
        time.sleep(5)  # Send a log every 5 seconds
