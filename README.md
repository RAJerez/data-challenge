# Data Challenge
I have solved an Alkemy challenge in which a project must be created that consumes data from
3 different sources to create a SQL database with cultural information
about Argentine libraries, museums and movie theaters.

## Extraction:
- The data is extracted and organized into routes following the following structure: “category\year-month\category-day-month-year.csv”.

## Data processing:
- All information from Museums, Movie Theaters and Libraries is normalized
Popular, to create a single table containing:
    - cod_localidad
    - id_provincia
    - id_departamento
    - categoría
    - provincia
    - localidad
    - nombre
    - domicilio
    - código postal
    - número de teléfono
    - mail
    - web

- The joint data is processed to be able to generate a table with the following
information:
    - Cantidad de registros totales por categoría
    - Cantidad de registros totales por fuente
    - Cantidad de registros por provincia y categoría

- The cinema information is processed to create a table that contains:
    - Provincia
    - Cantidad de pantallas
    - Cantidad de butacas
    - Cantidad de espacios INCAA


## Used tools:
- Python==3.10
- Poetry==1.7.1
- Postgres==13
- Docker==24.0.7

## Libraries used:
- pandas==2.1.4
- sqlalchemy==2.0.25
- psycopg2-binary==2.9.9
- click==8.1.7
- python-decouple==3.8
- requests==2.31.0
- ipykernel==6.28.0
- black==24.1.1


## Prerequisites to run the project
#### Poetry
Use Poetry for better dependency management and also to create my virtual environment.
Install poetry from pipx and the installation will be carried out isolated from the global environment
    
    pipx install poetry==1.7.1

To install the necessary dependencies described in pyproject.toml

    poetry install

A virtual environment will automatically be created that you can access

    poetry shell


#### Option with venv
If you do not use poetry you can install the dependencies through requirements.txt
The project was carried out with Python 3.10

    python3 -m virtualenv venv

    source venv/bin/activate

    pip install -r 'requirements.txt'


## Data Research
A pre-analysis of the datasource is carried out to know how the data is formed and the type of transformations that should be carried out.
You can see it in the jupyter-notebook file 'data_exploratory.ipynb'

## Creation of database, tables and pipeline execution
I build a container with Postgres Database:

    sudo docker compose up -d

You can access the database from bash:

    docker exec -it postgres psql -U postgres -d data-challenge

Create tables in database
The following script connects to the database and executes the script.sql stored in the data-challenge/sql folder.

    python3 script.py

In the following image you can see the creation of the necessary tables:
![Tablas_creadas](./images/tablas_creadas.png)

Run pipeline:

    python data-challenge/main.py --date YYYY-MM-DD

In the following image, queries are made in the database verifying that the transformation and loading have been carried out correctly:
![Verificacion](./images/verificacion.png)
