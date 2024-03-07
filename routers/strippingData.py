from pydantic import BaseModel
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy.orm import Session
from db import get_db
import models
from uuid import UUID
from datetime import date as Date, time
from routers import fermatation as Fermatation

class StrippingDataCreate(BaseModel):
    fermatationId: int
    date: Date
    startTime: time
    endTime: time
    washProcessed: float
    lowWineProduced : float
    startingTemprature : float
    startingProof : float
    endingTemprature : float
    endingProof : float
    wasteWaterTime : time
    wasteWaterTemprature : float
    wasteWaterPh : float
    flowRateRange : float
    wasteWaterToBufferTankDate : Date
    wasteWaterStorageLocation : str
    notes : str

class StrippingData(StrippingDataCreate):
    id: int
    uuid: UUID
    fermatation: Fermatation.Fermatation = {}

    class Config:
        orm_mode = True

router = CRUDRouter(
    schema=StrippingData,
    create_schema=StrippingDataCreate,
    db_model=models.StrippingData,
    db=get_db,
    prefix='strippingData'
)

# [...] get all records
@router.get('')
def get_StrippingData(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    strippingData = db.query(models.StrippingData).limit(limit).offset(skip).all()

    for p in strippingData:
        print(p, p.fermatation)
    return {'status': 'success', 'results': len(strippingData), 'strippingData': strippingData}

