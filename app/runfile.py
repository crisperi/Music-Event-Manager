#runfile.py
from models import engine, Base
from sqlalchemy.orm import sessionmaker
from models import Band, Venue,Concert


Base.metadata.create_all(engine)
    
Session= sessionmaker(bind=engine)
session = Session()

def create_instances():
    band1 = Band(name="Sonic Wave", hometown="Denver")
    band2 = Band(name="Echo Hunters", hometown="Los Angeles")
    band3 = Band(name="Silent Storm", hometown="Austin")
    band4 = Band(name="Neon Dreams", hometown="New York")
    band5 = Band(name="The Rolling Notes", hometown="San Francisco")

    venue1 = Venue(title="The Grand Hall", city="London")
    venue2 = Venue(title="Electric Arena", city="New York")
    venue3 = Venue(title="Skyline Stage", city="Phoenix")
    venue4 = Venue(title="Madison Square Garden", city="New York")
    venue5 = Venue(title="Underground Club", city="Boston")

    concert1 = Concert(date="2024-09-10", band=band1, venue=venue1)
    concert2 = Concert(date="2024-11-1", band=band2, venue=venue2)
    concert3 = Concert(date="2024-10-21", band=band4, venue=venue5)

    session.add_all([band1, band2, band3, band4, band5, venue1, venue2, venue3, venue4, venue5, concert1, concert2, concert3])
    session.commit()

def queries():
    most_performances = Band.most_performances(session)
    if most_performances:
        print(f"Band with the most performances: {most_performances.name}")

    concert = session.query(Concert).first()
    if concert:
        print(concert.introduction())
        
if __name__ == '__main__':
    #create_instances()
    queries()        