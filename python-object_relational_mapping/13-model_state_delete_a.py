#!/usr/bin/python3
"""Script to delete all State objects with a name containing the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> <password> <db_name>")
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create connection string
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}'
    )

    # Bind the engine to the metadata of the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State objects with names containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects
    for state in states_with_a:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
