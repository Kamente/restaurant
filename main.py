from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from customer import Customer, Base as CustomerBase
from restaurant import Restaurant, Base as RestaurantBase
from review import Review, Base as ReviewBase

DATABASE_URI = 'sqlite:///database.db'

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


CustomerBase.metadata.create_all(bind=engine)
RestaurantBase.metadata.create_all(bind=engine)
ReviewBase.metadata.create_all(bind=engine)
