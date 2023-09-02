from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, ForeignKey
from sqlalchemy.orm import session_maker, relationship

DATABASE_URI = 'sqlite:///restaurant.db'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()


