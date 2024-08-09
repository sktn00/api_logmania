import requests
import time
from datetime import datetime
from loguru import logger
import os
import random

API_KEY = os.getenv("SERVICE3_API_KEY")
SERVICE_NAME = "Service3"
BASE_URL = "http://localhost:8000"

logger.add(f"{SERVICE_NAME}.log", rotation="100 MB")

def generate_log():
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]
    users = ["Alice", "Bob", "Charlie", "David", "Eve"]
    actions = ["logged in", "logged out", "uploaded a file", "deleted a record", "updated their profile"]
    
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "service_name": SERVICE_NAME,
        "log_level": random.choice(log_levels),
        "message": f"User {random.choice(users)} {random.choice(actions)}"
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
        if random.random() < 0.7:  # 70% chance to generate a log
            log = generate_log()
            send_log(log)
        time.sleep(random.uniform(0.5, 5))  # Wait between 0.5 to 5 seconds before next iteration