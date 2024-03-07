from pydantic import BaseModel
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy.orm import Session
from db import get_db
import models
from uuid import UUID
from datetime import date, time

class FarmInspectionCreate(BaseModel):
    inspectionDate: date
    inspectionTime: time
    inspectionBy: str
    caneVarietySampled: models.CANE_VARIETY_SAMPLED_ENUM
    caneLengthJuiced: float
    juicedProduced: float
    gravityOfJuice: float
    isFertilizerUsed: bool
    evidenceOfPesticideUsed: bool
    evidenceOfUsedFertilizer: str
    typeOfPesticideUsed: models.PESTICIDE_USED_ENUM
    farmerId: int
    comments: str

class FarmInspection(FarmInspectionCreate):
    id: int
    uuid: UUID

    class Config:
        orm_mode = True

router = CRUDRouter(
    schema=FarmInspection,
    create_schema=FarmInspectionCreate,
    db_model=models.FarmInspection,
    db=get_db,
    prefix='farmInspection'
)

# [...] get all records
@router.get('')
def get_FarmInspection(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    farmInspections = db.query(models.FarmInspection).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(farmInspections), 'farmInspections': farmInspections}

