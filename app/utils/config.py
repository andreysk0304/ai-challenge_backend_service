import pytz

from os import getenv
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = getenv('DATABASE_URL')
REDIS_URL = getenv("REDIS_URL", "redis://redis:6379/0")

MOSCOW_TZ = pytz.timezone("Europe/Moscow")