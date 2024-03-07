from sqlalchemy import Column, ForeignKey, Identity, Integer, String, Boolean, Date, Time, Enum, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from db import Base
import enum
import uuid

class CANE_VARIETY_SAMPLED_ENUM(enum.Enum):
    Cane = 'Cane'
    Variety = 'Variety'
    Sampled = 'Sampled'

class PESTICIDE_USED_ENUM(enum.Enum):
    PesticideUsed = 'PesticideUsed'

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
    gravityOfJuice = Column(Numeric)
    isFertilizerUsed = Column(Boolean)
    evidenceOfUsedFertilizer = Column(String(255))
    evidenceOfPesticideUsed = Column(Boolean)
    typeOfPesticideUsed = Column(Enum(PESTICIDE_USED_ENUM))
    farmerId = Column(ForeignKey('farmers.id'), nullable=False)
    comments = Column(String(255))

    def __repr__(self):
        return 'FarmInspectionModel(uuid=%s, farmerId=%s)' % (self.uuid, self.farmerId)

class Harvesting(Base):
    __tablename__ = 'harvesting'

    id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    farmerId = Column(ForeignKey('farmers.id'), nullable=False)
    areaHarveted = Column(Numeric)
    startDate = Column(Date)
    endDate = Column(Date)
    weight = Column(Numeric)
    ratePerPound = Column(Numeric)
    specific = Column(Numeric)
    gravity = Column(Numeric)
    juiceDate = Column(Date)
    fermatationNo = Column(ForeignKey('fermatation.id'))

    fermatation = relationship("Fermatation", primaryjoin="Fermatation.id == Harvesting.fermatationNo")
    farmer = relationship("Farmers", primaryjoin="Farmers.id == Harvesting.farmerId")

    def __repr__(self):
        return 'HarvestingModel(uuid=%s, farmerId=%s)' % (self.uuid, self.farmerId)

class Fermatation(Base):
    __tablename__ = 'fermatation'

    id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    tankNumber = Column(String(255))
    startDate = Column(Date)
    endDate = Column(Date)
    yeastDose = Column(Numeric)
    nutrientDose = Column(Numeric)
    preparedBy = Column(String(255))

    harvesting = relationship("Harvesting", primaryjoin="Fermatation.id == Harvesting.fermatationNo",cascade="all, delete-orphan")
    chemistryLogs = relationship("ChemistryLogs", primaryjoin="Fermatation.id == ChemistryLogs.fermatationId",cascade="all, delete-orphan")
    strippingData = relationship("StrippingData", primaryjoin="Fermatation.id == StrippingData.fermatationId",cascade="all, delete-orphan")

    def __repr__(self):
        return 'FermatationModel(uuid=%s)' % (self.uuid)

class ChemistryLogs(Base):
    __tablename__ = 'chemistryLogs'

    id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    fermatationId = Column(ForeignKey('fermatation.id'), nullable=False)
    dateTime = Column(DateTime)
    specificGravity = Column(Numeric)
    temp = Column(Numeric)
    ph = Column(Numeric)
    preparedBy = Column(String(255))

    fermatation = relationship("Fermatation", primaryjoin="Fermatation.id == ChemistryLogs.fermatationId")

    def __repr__(self):
        return 'FermatationModel(uuid=%s)' % (self.uuid)
    
class StrippingData(Base):
    __tablename__ = 'strippingData'

    id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    uuid = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)
    fermatationId = Column(ForeignKey('fermatation.id'), nullable=False)
    date = Column(Date)
    startTime = Column(Time)
    endTime = Column(Time)
    washProcessed = Column(Numeric)
    lowWineProduced = Column(Numeric)
    startingTemprature = Column(Numeric)
    startingProof = Column(Numeric)
    endingTemprature = Column(Numeric)
    endingProof = Column(Numeric)
    wasteWaterTime = Column(Time)
    wasteWaterTemprature = Column(Numeric)
    wasteWaterPh = Column(Numeric)
    flowRateRange = Column(Numeric)
    wasteWaterToBufferTankDate = Column(Date)
    wasteWaterStorageLocation = Column(String(255))
    notes = Column(String(255))

    fermatation = relationship("Fermatation", primaryjoin="Fermatation.id == StrippingData.fermatationId")

    def __repr__(self):
        return 'FermatationModel(uuid=%s)' % (self.uuid)
