import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL")
    ENV = os.getenv("ENV")
    BROWSER = os.getenv("BROWSER")
    HEADLESS = os.getenv("HEADLESS")

    if not BASE_URL:
        raise ValueError("BASE_URL is not configured.")

    if not ENV:
        raise ValueError("ENV is not configured.")

    if not BROWSER:
        raise ValueError("BROWSER is not configured.")

    if BROWSER not in {"chromium", "firefox", "webkit"}:
        raise ValueError("Unsupported browser - Please choose chromium, firefox, or webkit.")

    if HEADLESS not in {"true", "false"}:
        raise ValueError("HEADLESS must be either 'true' or 'false'.")

    HEADLESS = HEADLESS == "true"
