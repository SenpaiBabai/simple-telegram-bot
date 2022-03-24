from sqlalchemy import create_engine

engine = create_engine(
    "psycopg2://scott:tiger@localhost/test",
)