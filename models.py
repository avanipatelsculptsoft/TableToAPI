from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Boolean, Date, Time, Enum, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from db import Base
import enum
import uuid

class CANE_VARIETY_SAMPLED_ENUM(enum.Enum):
    CANE = 'Cane'
    VARIETY = 'Variety'
    SAMPLED = 'Sampled'

class PESTICIDE_USED_ENUM(enum.Enum):
    PESTICIDE_USED = 'PesticideUsed'

class Farmers(Base):
    __tablename__ = 'farmers'

    id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=False)
    village = Column(String(255), nullable=False)
    phone = Column(String(15))
    contractSigned = Column(Boolean)
    acreAge = Column(Numeric)
    totalAcres = Column(Numeric)

    farmInspections = relationship("FarmInspection", primaryjoin="Farmers.id == FarmInspection.farmerId",cascade="all, delete-orphan")

    def __repr__(self):
        return 'FarmersModel(firstName=%s, lastName=%s,uuid=%s)' % (self.firstName, self.lastName,self.uuid)

class FarmInspection(Base):
    __tablename__ = 'farmInspection'

    id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    inspectionDate = Column(Date)
    inspectionTime = Column(Time)
    inspectionBy = Column(String(255))
    caneVarietySampled = Column(Enum(CANE_VARIETY_SAMPLED_ENUM))
    caneLengthJuiced = Column(Numeric)
    juicedProduced = Column(Numeric)
    gravityofJuice = Column(Numeric)
    isFertilizerUsed = Column(Boolean)
    evidenceOfUsedFertilizer = Column(String(255))
    evidenceOfPesticideUsed = Column(Boolean)
    typeOfPesticideUsed = Column(Enum(PESTICIDE_USED_ENUM))
    farmerId = Column(ForeignKey('farmers.id'), nullable=False)
    comments = Column(String(255))

    def __repr__(self):
        return 'FarmInspectionModel(uuid=%s, farmerId=%s)' % (self.uuid, self.farmerId)
