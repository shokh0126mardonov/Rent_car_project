from enum import Enum
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Boolean,
    Enum as SQLEnum
)


from ..db.database import Base


class UserRole(Enum):
    user = "user"
    admin = "admin"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    name = Column(String)
    is_verified = Column(Boolean, default=False)
    verification_code = Column(Integer)
    role = Column(SQLEnum(UserRole), default=UserRole.user)
  
    def __repr__(self):
        return f"User(id = {self.id}, email = {self.email}, name = {self.name}, phone = {self.phone})"