from models.akonta import AkontaObject
from models.category import AkontaCategory
from extras.tools import product_code_generator
from peewee import *


class AkontaProduct(AkontaObject):
    """
        Represente un produit
    """
    name = CharField(max_length=150)
    description = TextField(null=True)
    category = ForeignKeyField(AkontaCategory, backref="products")
    code = CharField(default=product_code_generator, unique=True, index=True)
    image = CharField(max_length=500, null=True)
    price = DecimalField(decimal_places=2)
    cost = DecimalField(decimal_places=2, null=True)

    def __str__(self):
        return f"{self.code} -> {self.name}"
