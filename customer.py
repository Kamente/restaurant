from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    cust_id = Column(Integer, Sequence('cust_id_seq'), primary_key=True)
    cust_fname = Column(String)
    cust_lname = Column(String)

    reviews = relationship('Review', back_populates='customer')
