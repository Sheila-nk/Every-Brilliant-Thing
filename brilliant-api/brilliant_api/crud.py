"""
In this file we will have reusable functions to interact with the data in the database.
CRUD comes from: Create, Read, Update, and Delete.
This program only utilizes Create and Read
"""

from tortoise.expressions import RawSQL

from .models import BrilliantThing
from . import schemas


async def get_brilliant_thing():
    # query database for all brilliant thing entries
    brilliant_thing = await BrilliantThing.all().annotate(order=RawSQL("RANDOM()")).order_by("order").first()

    # return a random brilliant thing
    return brilliant_thing


async def create_brilliant_thing(brilliant_thing: schemas.BrilliantThingCreate):
    # add a brilliant thing entry to database
    new_entry = await BrilliantThing.create(entry=brilliant_thing.entry)

    # return brilliant thing added: "Brilliant thing #123"
    return new_entry
