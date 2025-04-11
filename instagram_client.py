import logging
from instagrapi import Client
from config import (
    INSTAGRAM_USERNAME, 
    INSTAGRAM_PASSWORD, 
    INSTAGRAM_APP_ID, 
    INSTAGRAM_APP_SECRET
)
from utils import random_delay

class InstagramClient:
    def __init__(self):
        self.client = Client()
        self.client.set_settings({
            "app_id": INSTAGRAM_APP_ID,
            "app_secret": INSTAGRAM_APP_SECRET
        })

    def login(self):
        random_delay(30, 60)
        try:
            self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
            logging.info("✅ Successfully logged into Instagram")
        except Exception as e:
            logging.error(f"❌ Login failed: {e}")
            raise e

    def fetch_unread_threads(self):
        try:
            inbox_threads = self.client.direct_threads(selected_filter='unread')
            unread_threads = [thread for thread in inbox_threads if thread.messages]
            logging.info(f"📩 Found {len(unread_threads)} unread threads")
            return unread_threads
        except Exception as e:
            logging.error(f"❌ Error fetching threads: {e}")
            return []

    def send_message(self, thread_id, message):
        try:
            self.client.direct_send(message, thread_ids=[thread_id])
            logging.info(f"✉️ Sent response to thread {thread_id}")
        except Exception as e:
            logging.error(f"❌ Failed to send message: {e}")
