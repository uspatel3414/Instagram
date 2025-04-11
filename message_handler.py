import logging
from utils import random_delay

def reply_to_unread_messages(instagram_client):
    unread_threads = instagram_client.fetch_unread_threads()
    for thread in unread_threads:
        try:
            instagram_client.send_message(thread.id, "❤️")
            random_delay(5, 15)
        except Exception as e:
            logging.error(f"❌ Error replying in thread {thread.id}: {e}")
