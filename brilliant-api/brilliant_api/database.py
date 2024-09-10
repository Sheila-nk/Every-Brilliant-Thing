import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.environ['SQLALCHEMY_DATABASE_URL']

# Create an SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class. Each instance of the SessionLocal class will be a database session. 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class. We will inherit from this class to create each of the database models.
Base = declarative_base()
