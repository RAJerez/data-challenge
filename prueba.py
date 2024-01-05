from pathlib import Path

BASE_FILE_DIR = Path("/tmp")
ROOT_DIR = Path().resolve().parent
SQL_DIR = ROOT_DIR / "data-challenge/sql"

print(f'BASE_FILE_DIR = {BASE_FILE_DIR}')
print(f'ROOT_DIR = {ROOT_DIR}')
print(f'SQL_DIR = {SQL_DIR}')
