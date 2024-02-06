import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from constants import SQL_DIR, TABLE_NAMES
from cfg import DB_CONNSTR
import logging


logging.basicConfig(level=logging.DEBUG)

engine = create_engine(DB_CONNSTR)
log = logging.getLogger()


def create_tables():
    """Create db tables"""
    try:
        with engine.connect() as con:
            for file in TABLE_NAMES:
                log.info(f"Creating table {file}")
                with open(SQL_DIR / f"{file}.sql") as f:
                    query = text(f.read())
                    log.debug(f"Query for {file}: {query}")

                # con.execute(f"DROP TABLE IF EXISTS {file}")
                con.execute(query)
                con.commit()
        log.info("Tables created successfully.")

    except sa.exc.SQLAlchemyError as e:
        # Errores específicos de SQLAlchemy
        log.info(f"Error creating tables: {e}")
    except Exception as e:
        # Excepciones generales
        log.info(f"Unexpected error: {e}")


if __name__ == "__main__":
    create_tables()
