from pydantic import BaseModel
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter as CRUDRouter
from sqlalchemy.orm import Session
from db import get_db
import models
from uuid import UUID
from datetime import datetime
from routers import fermatation as Fermatation

class ChemistryLogsCreate(BaseModel):
    fermatationId : int
    dateTime : datetime
    specificGravity : float
    temp : float
    ph : float
    preparedBy : str

class ChemistryLogs(ChemistryLogsCreate):
    id: int
    uuid: UUID
    fermatation: Fermatation.Fermatation = {}

    class Config:
        orm_mode = True

router = CRUDRouter(
    schema=ChemistryLogs,
    create_schema=ChemistryLogsCreate,
    db_model=models.ChemistryLogs,
    db=get_db,
    prefix='chemistryLogs'
)

# [...] get all records
@router.get('')
def get_ChemistryLogs(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit

    chemistryLogs = db.query(models.ChemistryLogs).limit(limit).offset(skip).all()

    for p in chemistryLogs:
        print(p, p.fermatation)
    return {'status': 'success', 'results': len(chemistryLogs), 'chemistryLogs': chemistryLogs}

