from decouple import AutoConfig
from constants import ROOT_DIR

config = AutoConfig(search_path=ROOT_DIR)

# Levanto las variables desde settings.ini
DB_CONNSTR = config("DB_CONNSTR")
MUSEO_URL = config("MUSEO_URL")
CINE_URL = config("CINE_URL")
BIBLIOTECA_URL = config("BIBLIOTECA_URL")

# diccionarios con {nombres de 'data src' y URL}
museo_ds = {
    "name" : "museo",
    "url" : MUSEO_URL
}

cine_ds = {
    "name" : "cines",
    "url" : CINE_URL
}

biblioteca_ds = {
    "name" : "bibliotecas_populares",
    "url" : BIBLIOTECA_URL
}