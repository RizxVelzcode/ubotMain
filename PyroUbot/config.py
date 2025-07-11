import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "7066156416").split()))

API_ID = int(os.getenv("API_ID", "23762137"))

API_HASH = os.getenv("API_HASH", "2fb2beeec1e3eac802cfd824690df492")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7810313771:AAFwUdq6YcMFCvlhjD_3tPo7U2Q28VsOz7U")

OWNER_ID = int(os.getenv("OWNER_ID", "7066156416"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ml9079716:48gxGsQhTHWumLI15@cluster0.6e1q9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002323130008"))
