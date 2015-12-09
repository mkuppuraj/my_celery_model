import os

from phonebook.model.phone import Phone
from phonebook.model.contact import Contact

from phonebook.model.base import Base

def create_tables():
    db_path = os.environ['PHONEBOOK_DB']
    engine = create_engine("sqlite://%s" % db_path)
    Base.metadata.create_all(engine)
