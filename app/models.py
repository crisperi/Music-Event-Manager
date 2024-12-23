from sqlalchemy import (Column, Integer, 
String,ForeignKey,create_engine, func)
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///concerts.db")


Base = declarative_base()


class Band(Base):
    __tablename__='bands'
    
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    hometown = Column(String())
    
    concerts = relationship("Concert", back_populates='band')
    
    def __repr__(self):
        return f"<Band(name={self.name}, hometown={self.hometown})>"
    
    def venues(self):
        return [concert.venue for concert in self.concerts]
    
    @classmethod
    def most_performances(cls, session):
        return (session.query(cls).join(Concert).group_by(cls.id)
                .order_by(func.count(Concert.id).desc())
                .first())
        

class Venue(Base):
    __tablename__ = "venues"
    
    id = Column(Integer(), primary_key = True)
    title = Column(String())
    city = Column(String())
    
    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f"<Venue(title={self.title}, city={self.city})>"

    def bands(self):
        return [concert.band for concert in self.concerts]