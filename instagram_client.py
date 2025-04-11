import logging
import os
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
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
        self.session_file = "session.json"
        self.client.set_settings({
            "app_id": INSTAGRAM_APP_ID,
            "app_secret": INSTAGRAM_APP_SECRET,
            "device_settings": {
                "app_version": "269.0.0.18.75",
                "android_version": 25,
                "android_release": "7.1.2",
                "phone_manufacturer": "OnePlus",
                "phone_device": "ONEPLUS A6013",
                "phone_model": "ONEPLUS 6T Dev",
                "phone_dpi": "380dpi"
            }
        })

    def login(self):
        try:
            if os.path.exists(self.session_file):
                self.client.load_settings(self.session_file)
                self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
                logging.info("✅ Session loaded successfully")
            else:
                random_delay(30, 60)
                self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
                self.client.dump_settings(self.session_file)
                logging.info("✅ New session created")
        except LoginRequired:
            logging.error("❌ Session expired - creating new session")
            self.client.relogin()
            self.client.dump_settings(self.session_file)
        except Exception as e:
            logging.error(f"❌ Login failed: {str(e)}")
            raise e
