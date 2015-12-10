import os

from phonebook.core.db import create_engine

from phonebook.model.phone import Phone
from phonebook.model.contact import Contact
from phonebook.model.base import Base

def initialize():
    engine = create_engine()
    Base.metadata.create_all(engine)
