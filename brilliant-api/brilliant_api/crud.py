"""
In this file we will have reusable functions to interact with the data in the database.
CRUD comes from: Create, Read, Update, and Delete.
This program only utilizes Create and Read
"""

from sqlalchemy.orm import Session
from sqlalchemy import func
from random import randint

import models
import schemas


def get_brilliant_thing(db: Session):
    # query database for all brilliant thing entries
    brilliant_thing = db.query(models.BrilliantThing).order_by(func.random()).first()

    # return a random brilliant thing
    return brilliant_thing


def create_brilliant_thing(db: Session, brilliant_thing: schemas.BrilliantThingCreate):
    # add a brilliant thing entry to database
    new_entry = models.BrilliantThing(entry=brilliant_thing.entry)

    db.add(new_entry)
    db.commit()

    # refresh your instance so that it contains any new data from the database
    db.refresh(new_entry)

    # return brilliant thing added: "Brilliant thing #123"
    return new_entry
