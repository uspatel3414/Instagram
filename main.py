import logging
import time
from instagram_client import InstagramClient
from message_handler import reply_to_unread_messages
from utils import setup_logging

def main():
    setup_logging()
    logging.info("🚀 Starting Instagram Bot Service")
    
    instagram_client = InstagramClient()
    
    while True:
        try:
            # Attempt login
            instagram_client.login()
            
            # Process messages
            reply_to_unread_messages(instagram_client)
            
            # Sleep before next check (5 minutes)
            logging.info("⏸️ Next check in 5 minutes...")
            time.sleep(300)
            
        except Exception as e:
            logging.error(f"❌ Critical error: {e}")
            logging.info("🔄 Retrying in 1 minute...")
            time.sleep(60)

if __name__ == "__main__":
    main()
