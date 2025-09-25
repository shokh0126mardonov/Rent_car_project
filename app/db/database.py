from sqlalchemy import URL ,create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from ..core import DB_HOST,DB_NAME,DB_PASSWORD,DB_PORT,DB_USER

url_object = URL.create(
    "postgresql+psycopg2",
    host=DB_HOST,
    username=DB_USER,
    port=DB_PORT,
    password=DB_PASSWORD,
    database=DB_NAME
)

engine = create_engine(url_object)

LocalSession = sessionmaker(autoflush=True,autocommit = True,bind=engine)
Base = declarative_base()