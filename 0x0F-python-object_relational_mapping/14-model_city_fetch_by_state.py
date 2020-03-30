#!/usr/bin/python3
"""
That deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    state_rows = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id)
    for item in state_rows:
        print(item[1].name + ": (" + str(item[0].id) + ") " + item[0].name)
