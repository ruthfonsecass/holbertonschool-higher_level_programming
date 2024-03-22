#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')


    Base.metadata.create_all = engine

    
    DBSession = sessionmaker(bind=engine)
    
    # Create a session
    session = DBSession()

    # Query all states
    states = session.query(State).order_by(State.id).all()

    # Print states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()