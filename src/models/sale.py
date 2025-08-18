from models.akonta import AkontaObject
from models.product import AkontaProduct
from extras.tools import sale_code_generator
from peewee import *


class AkontaSale(AkontaObject):
    amount = DecimalField(decimal_places=2)
    code = CharField(default=sale_code_generator)

    def __str__(self):
        return self.code



class AkontaSaleItem(AkontaObject):
    sale = ForeignKeyField(AkontaSale, backref='items')
    product = ForeignKeyField(AkontaProduct)
    quantity = IntegerField(default=1)
    price = DecimalField(decimal_places=2)
    comment = TextField(null=True)

    def __str__(self):
        return f"{self.sale.code} -> {self.product.name} x {self.quantity}"
