from sqlalchemy import Column, ForeignKey, Identity, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    customer_name = Column(String(255), nullable=False)

    contacts = relationship('Contacts', back_populates='customer')


class Contacts(Base):
    __tablename__ = 'contacts'

    contact_id = Column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    contact_name = Column(String(255), nullable=False)
    customer_id = Column(ForeignKey('customers.customer_id'))
    phone = Column(String(15))
    email = Column(String(100))

    customer = relationship('Customers', back_populates='contacts')
