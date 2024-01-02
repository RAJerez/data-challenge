Using poetry install it will create a virtualenv with all the necesary dependencies then you can access it with poetry shell.
If you need to add a dependency just use poetry add <dependency> or you can customice much more editing the pyproyect.toml



Contenedor postgres:

    docker run -d --name challenge_pg -v my_dbdata:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=data_analytics postgres:13

Acceder:

    docker exec -it challenge_pg psql -U postgres -d data_analytics

Crear base de Datos:

    python3 script.py