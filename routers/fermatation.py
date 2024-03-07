from pydantic import BaseModel
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy.orm import Session
from db import get_db
import models
from uuid import UUID
from datetime import date

class FermatationCreate(BaseModel):
    tankNumber : str
    startDate : date
    endDate : date
    yeastDose : float
    nutrientDose : float
    preparedBy : str

class Fermatation(FermatationCreate):
    id: int
    uuid: UUID

    class Config:
        orm_mode = True

router = CRUDRouter(
    schema=Fermatation,
    create_schema=FermatationCreate,
    db_model=models.Fermatation,
    db=get_db,
    prefix='fermatation'
)

# [...] get all records
@router.get('')
def get_Fermatation(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    fermatation = db.query(models.Fermatation).limit(limit).offset(skip).all()

    return {'status': 'success', 'results': len(fermatation), 'fermatations': fermatation}

