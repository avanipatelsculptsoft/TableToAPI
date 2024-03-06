from pydantic import BaseModel
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy.orm import Session
from db import get_db
import models
from uuid import UUID
from typing import List
from routers import farmInspection

class FarmersCreate(BaseModel):
    firstName: str
    lastName: str
    village: str
    phone: str
    contractSigned: bool
    acreAge: float
    totalAcres: float

class Farmers(FarmersCreate):
    id: int
    uuid: UUID
    farmInspections: List[farmInspection.FarmInspection] = []

    class Config:
        orm_mode = True

router = CRUDRouter(
    schema=Farmers,
    create_schema=FarmersCreate,
    db_model=models.Farmers,
    db=get_db,
    prefix='farmer'
)

# [...] get all records
@router.get('')
def get_Farmers(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    farmers = db.query(models.Farmers).join(models.FarmInspection).filter(
        models.Farmers.firstName.contains(search)).limit(limit).offset(skip).all()

    for p in farmers:
        print(p, p.farmInspections)
    return {'status': 'success', 'results': len(farmers), 'farmers': farmers}

