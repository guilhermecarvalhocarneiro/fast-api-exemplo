import uuid
import datetime

from typing import Generator

from sqlalchemy import create_engine, Column,String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from .config import settings

'''
Arquivo responsável pelo banco de dados

- Model principal que será herdado pelos outros models de outras app
- Cria uma instância do banco e finaliza ao finalizar a transação
'''

@as_declarative()
class Base:
    id = Column(String, primary_key=True, default=uuid.uuid4, nullable=False)
    deleted = Column(Boolean, default=False, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_on = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


SQLALCHEMY_DATABASE_URI: str = f"{settings.db_connection}://{settings.db_username}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_database}"

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()