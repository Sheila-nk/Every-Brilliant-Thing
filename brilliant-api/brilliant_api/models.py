from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


# Create SQLAlchemy models from the Base class
class BrilliantThing(Base):
    __tablename__ = "brilliant_things"

    id = Column(Integer, primary_key=True)
    entry = Column(String)
    date_posted = Column(DateTime, default=datetime.utcnow)

