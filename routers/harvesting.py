from pydantic import BaseModel
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy.orm import Session
from db import get_db
import models
from uuid import UUID
from datetime import date
from routers import farmers, fermatation as Fermatation

class HarvestingCreate(BaseModel):
    farmerId : int
    fermatationNo : int
    areaHarveted : float 
    startDate : date
    endDate : date
    weight : float
    ratePerPound : float 
    specific : float
    gravity : float
    juiceDate : date

class Harvesting(HarvestingCreate):
    id: int
    uuid: UUID
    farmer: farmers.Farmers = {}
    fermatation: Fermatation.Fermatation = {}

    class Config:
        orm_mode = True

router = CRUDRouter(
    schema=Harvesting,
    create_schema=HarvestingCreate,
    db_model=models.Harvesting,
    db=get_db,
    prefix='harvesting'
)

# [...] get all records
@router.get('')
def get_Harvesting(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    harvesting = db.query(models.Harvesting).join(models.Farmers).join(models.Fermatation).limit(limit).offset(skip).all()

    for p in harvesting:
        print(p, p.farmer)
        print(p, p.fermatation)
    return {'status': 'success', 'results': len(harvesting), 'harvesting': harvesting}

