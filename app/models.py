from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.orm import declarative_base, relationship, validates, sessionmaker
from os.path import join, dirname, abspath
from datetime import datetime

# Database configuration
current_dir = dirname(abspath(__file__))
database_path = join(current_dir, '..', 'concerts.db')

engine = create_engine(f"sqlite:///{database_path}")
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Utility functions
def validate_date(date_str):
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Models
class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship("Concert", back_populates='band')

    def __repr__(self):
        return f"<Band(name={self.name}, hometown={self.hometown})>"

    def venues(self):
        return [concert.venue for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        return (
            session.query(cls)
            .join(Concert)
            .group_by(cls.id)
            .order_by(func.count(Concert.id).desc())
            .first()
        )

    @validates('name', 'hometown')
    def validate_fields(self, key, value):
        if not value or not value.strip():
            raise ValueError(f"{key} cannot be empty")
        return value.strip()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "hometown": self.hometown,
            "concerts": len(self.concerts),
        }


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f"<Venue(title={self.title}, city={self.city})>"

    @validates('title', 'city')
    def validate_fields(self, key, value):
        if not value or not value.strip():
            raise ValueError(f"{key} cannot be empty")
        return value.strip()

    def bands(self):
        return [concert.band for concert in self.concerts]

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "city": self.city,
            "concerts": len(self.concerts),
        }


class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)

    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    @validates('date')
    def validate_date(self, key, date_str):
        if not validate_date(date_str):
            raise ValueError("Invalid date format")
        return date_str

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "band": self.band.to_dict() if self.band else None,
            "venue": self.venue.to_dict() if self.venue else None,
        }
