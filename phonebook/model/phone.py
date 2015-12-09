from sqlalchemy import Column, Integer, String

from phonebook.model.base import Base

class Phone(Base):
    
    __tablename__ = 'phone'

    phone_idn = Column(Integer, primary_key=True)
    phone_number = Column(Number)
    phone_type = Column(String)
    is_active = Column(Number)
    country = Column(String)
    country_code = Column(String)
