from fastapi import FastAPI
from .db.create_tables import create_table

app = FastAPI(title="Rent Car API",relod = True)
create_table()