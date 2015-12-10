from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = None
Session = None

def create_engine():
    phonebook_db = os.environ['PHONEBOOK_DB']
    if not engine:
        engine = create_engine("sqlite:///%s" % phonebook_db)
    return engine

def create_session():
    if not Session:
        engine = create_engine()
        Session = sessionmaker(bind=engine)
    return Session.session()
