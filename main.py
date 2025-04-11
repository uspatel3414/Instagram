import logging
import time
from instagram_client import InstagramClient
from message_handler import reply_to_unread_messages
from utils import setup_logging, validate_env

def main():
    setup_logging()
    logging.info("🚀 Starting Instagram Bot Service")
    
    try:
        validate_env()
        instagram_client = InstagramClient()
        
        while True:
            try:
                instagram_client.login()
                reply_to_unread_messages(instagram_client)
                logging.info("⏸️ Next check in 5 minutes...")
                time.sleep(300)
                
            except Exception as e:
                logging.error(f"❌ Critical error: {e}")
                logging.info("🔄 Retrying in 1 minute...")
                time.sleep(60)
                
    except Exception as e:
        logging.error(f"🔥 Fatal initialization error: {e}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
