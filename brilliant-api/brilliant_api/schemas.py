
"""
Note: The file `models.py` has the SQLAlchemy models, and the file `schemas.py` has the Pydantic models.
These Pydantic models define more or less a "schema" (a valid data shape).
"""

from pydantic import BaseModel
from datetime import datetime

class BrilliantThingBase(BaseModel):
    entry: str


class BrilliantThingCreate(BrilliantThingBase):
    pass


class BrilliantThing(BrilliantThingBase):
    id: int
    date_posted: datetime

    class Config:
        """
        Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, 
        but an ORM model (or any other arbitrary object with attributes).
        This way, instead of only trying to get the id value from a dict, as in: id = data["id"],
        it will also try to get it from an attribute, as in: id = data.id
        """
        orm_mode = True