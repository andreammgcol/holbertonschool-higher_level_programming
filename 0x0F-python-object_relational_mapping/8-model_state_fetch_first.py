#!/usr/bin/python3
"""
That prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    state_rows = session.query(State).first()
    if state_rows:
        print(str(state_rows.id) + ": " + state_rows.name)
    else:
        print("Nothing")
