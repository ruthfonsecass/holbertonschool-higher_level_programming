from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of the declarative base class
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

# Database connection details
username = 'your_username'
password = 'your_password'
database_name = 'your_database_name'

# Connect to the MySQL database
engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}', echo=True)

# Ensure all classes inheriting from Base are imported before this line
Base.metadata.create_all(engine)

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)
session = Session()