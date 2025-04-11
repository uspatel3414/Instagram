import time
import random
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def random_delay(min_seconds, max_seconds):
    delay = random.randint(min_seconds, max_seconds)
    logging.info(f"⏳ Waiting {delay} seconds...")
    time.sleep(delay)
