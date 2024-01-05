from decouple import AutoConfig
from constants import ROOT_DIR

config = AutoConfig(search_path=ROOT_DIR)

# Levanto las variables desde settings.ini
DB_CONNSTR = config("DB_CONNSTR")
MUSEO_URL = config("MUSEO_URL")
CINES_URL = config("CINES_URL")
ESPACIOS_URL = config("ESPACIOS_URL")

# diccionarios con {nombres de data src : URL}
museo_ds = {
    "name" : "museo",
    "url" : MUSEO_URL
}

cines_ds = {
    "cines" : "cines",
    "url" : CINES_URL
}

espacios_ds = {
    "name" : "bibliotecas_populares",
    "url" : ESPACIOS_URL
}