from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from phonebook.model.base import Base

class Phone(Base):

    __tablename__ = 'phone'

    phone_idn = Column(Integer, primary_key=True)
    phone_number = Column(Integer)
    phone_type = Column(String)
    is_active = Column(Integer)
    country = Column(String)
    country_code = Column(String)

    contact = relationship("Contact", backref=backref('addresses', order_by=id))
