
from pathlib import Path
from peewee import SqliteDatabase
from .category import AkontaCategory
from .product import AkontaProduct
from .customer import AkontaCustomer
from .invoice import AkontaInvoice
from .sale import AkontaSale, AkontaSaleItem
from .shop import AkontaShop
from .transaction import AkontaTransaction

db_path = Path(__file__).parent.parent.joinpath('db/akonta.db')
db = SqliteDatabase(db_path)


def db_initializer():
    db.connect()
    db.create_tables([AkontaCategory, AkontaCustomer, AkontaProduct, AkontaInvoice, AkontaSale, AkontaSaleItem, AkontaShop, AkontaTransaction])
