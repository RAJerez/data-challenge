from pathlib import Path

BASE_FILE_DIR = Path("/tmp") # donde almaceno los archivos
ROOT_DIR = Path().resolve().parent # ruta padre donde se encuentra mi proyecto
SQL_DIR = ROOT_DIR / "data-challenge/sql" # ruta donde estan mis archivos sql
SETTINGS_DIR = ROOT_DIR / "data-challenge"

# Nombres de tablas
RAW_TABLE_NAME = "raw"
CINE_INSIGHTS_TABLE_NAME = "cine_insights"
SOURCE_SIZE_TABLE_NAME = "size_by_datasource"
CATEGORY_COUNT_TABLE_NAME = "size_by_category"
PROV_CAT_COUNT_TABLE_NAME = "size_by_prov_category"

# Lista con nombres de las tablas
TABLE_NAMES = [
    RAW_TABLE_NAME,
    CINE_INSIGHTS_TABLE_NAME,
    SOURCE_SIZE_TABLE_NAME,
    CATEGORY_COUNT_TABLE_NAME,
    PROV_CAT_COUNT_TABLE_NAME
]