from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from phonebook.model.base import Base

class Contact(Base):

    __tablename__ = 'contact'

    contact_idn = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)

    phones = relationship("Phone", order_by="Phone.phone_id", backref="Contact")
