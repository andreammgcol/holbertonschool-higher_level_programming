#!/usr/bin/python3
"""
That adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    state_rows = session.query(State).order_by(State.id)
    for item in state_rows:
        new_id = item.id
    print(str(new_id))
