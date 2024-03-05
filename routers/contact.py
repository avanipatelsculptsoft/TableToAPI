from pydantic import BaseModel
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

class ContactsCreate(BaseModel):
    contact_name: str
    customer_id: int
    phone: str
    email: str

class Contacts(ContactsCreate):
    contact_id: int

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
    schema=Contacts,
    create_schema=ContactsCreate,
    db_model=models.Contacts,
    db=get_db,
    prefix='contact'
)