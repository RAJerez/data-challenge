from decouple import AutoConfig
from constants import SETTINGS_DIR

config = AutoConfig(search_path=SETTINGS_DIR)

# Levanto las variables desde settings.ini
DB_CONNSTR = config("DB_CONNSTR")
MUSEO_URL = config("MUSEO_URL")
CINE_URL = config("CINE_URL")
BIBLIOTECA_URL = config("BIBLIOTECA_URL")

print(DB_CONNSTR)
