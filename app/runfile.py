#runfile.py
from models import engine, Base
from sqlalchemy.orm import sessionmaker
from models import Band, Venue,Concert


Base.metadata.create_all(engine)
    
Session= sessionmaker(bind=engine)
session = Session()
