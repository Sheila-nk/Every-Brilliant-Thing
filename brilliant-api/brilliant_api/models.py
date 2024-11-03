from tortoise import fields
from tortoise.models import Model


class BrilliantThing(Model):
    id = fields.IntField(primary_key=True)
    entry = fields.CharField(max_length=1000)
    date_posted = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.entry

