from decouple import AutoConfig
from constants import SETTINGS_DIR

config = AutoConfig(search_path=SETTINGS_DIR)

# I raise the variables from settings.ini
DB_CONNSTR = config("DB_CONNSTR")
MUSEO_URL = config("MUSEO_URL")
CINE_URL = config("CINE_URL")
BIBLIOTECA_URL = config("BIBLIOTECA_URL")

# dictionaries with data sources names and URLs
museo_ds = {"name": "museo", "url": MUSEO_URL}

cine_ds = {"name": "cine", "url": CINE_URL}

biblioteca_ds = {"name": "biblioteca_popular", "url": BIBLIOTECA_URL}
