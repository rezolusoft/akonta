from models.akonta import AkontaObject
from extras.enums import TransactionTypeEnums
from peewee import *

class AkontaTransaction(AkontaObject):
    title = CharField()
    amount = DecimalField()
    type = CharField(choices=TransactionTypeEnums.items())
    description = TextField(null=True)

    def __str__(self):
        return f"{self.title} -> {self.amount}"
