from ..models.user import User
from .database import Base,declarative_base,engine

def create_table():
    Base.metadata.create_all(engine) 
    