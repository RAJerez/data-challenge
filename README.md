# Data Challenge

## Prerequisitos
#### Poetry
Utilizé Poetry para un mejor manejo de dependecias y también para crear mi entorno virtual.

Instalar poetry desde pipx y la instalación se realizara aislada del entorno global
    
    pipx install poetry

Para instalar las dependencias necesarias descriptas en pyproyect.toml

    poetry install

Automaticamente se creara un entorno virtual al cual puede acceder

    poetry shell


#### Opción sin Poetry
En caso de no usar poetry puede instalar las dependencias a traves de requirements.txt
El proyecto se realizó con Python 3.10

    python3 -m virtualenv venv

    source venv/bin/activate

    pip install -r 'requirements.txt'


## Data Research
Se realiza un pre-análisis del datasource para saber el tipo de transformaciones que se deberia realizar
Puede verlo en el archivo jupyter-notebook 'data_exploratory.ipynb'

## Creación de base de datos, tablas y ejecución de pipeline
Levanto contenedor con Base de datos Postgres:

    sudo docker compose up -d

Puede acceder a la base de datos desde bash:

    docker exec -it postgres psql -U postgres -d data-challenge

Crear de tablas en base de datos
El siguiente script realiza la conexión con la base de datos y ejecuta los script.sql almacenados en la carpeta data-challenge/sql

    python3 script.py

Ejecutar pipeline:

    python data-challenge/main.py --date YYYY-MM-DD