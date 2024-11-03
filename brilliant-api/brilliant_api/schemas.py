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
        from_attributes = True