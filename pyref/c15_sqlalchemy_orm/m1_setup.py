"""Using SQLAlchemy ORM to Connect to a Database and Create a Table"""

from . import ENGINE, METADATA, SESSION

if __name__ == "__main__":
    session = SESSION()
    try:
        METADATA.drop_all(ENGINE, checkfirst=True)
        print("Existing tables dropped successfully.")
        METADATA.create_all(ENGINE, checkfirst=True)
        print("Tables created successfully.")
        session.commit()  # commit trasaction
    finally:
        session.close()  # close session
