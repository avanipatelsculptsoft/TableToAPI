from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

class CustomersCreate(BaseModel):
    customer_name: str

class Customers(CustomersCreate):
    customer_id: int

    class Config:
        orm_mode = True

engine = create_engine(
    "postgresql+pg8000://postgres:password@localhost:5433/codegendb"
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()

models.Base.metadata.create_all(bind=engine)
router = CRUDRouter(
    schema=Customers,
    create_schema=CustomersCreate,
    db_model=models.Customers,
    db=get_db,
    prefix='customer'
)