from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    rest_id = Column(Integer, Sequence('rest_id_seq'), primary_key=True)
    rest_name = Column(String)
    rest_price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
