from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/d0fe6e8f4bdb90919276c.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/2fcd27c7ee0c4cf0f2be9.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ARYANSTUDYGROUP")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AboutInnocent")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5968675414").split()))


FAILED = "https://telegra.ph/file/db8765da6945e3c9333e6.jpg"
