from pathlib import Path
import logging
from peewee import SqliteDatabase
from .category import AkontaCategory
from .product import AkontaProduct
from .customer import AkontaCustomer
from .invoice import AkontaInvoice
from .sale import AkontaSale, AkontaSaleItem
from .shop import AkontaShop
from .transaction import AkontaTransaction
from extras.store import AkontaStore

# initialiser la base de donnée
db_path = Path(__file__).parent.parent.joinpath('db/akonta.db')
db = SqliteDatabase(db_path)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def db_initializer(page):

    store = AkontaStore(page)

    db_init = store.get("db_init")

    tables=[AkontaCategory, 
            AkontaCustomer, 
            AkontaProduct, 
            AkontaInvoice, 
            AkontaSale, 
            AkontaSaleItem, 
            AkontaShop, 
            AkontaTransaction]

    if not db_init:

        logging.info("##### DB INITIALIZATION #####")

        db.connect() # connection a la db
        db.create_tables(tables) # creation des tables

        store.set("db_init", True)

        logging.info("##### DB INITIALIZED SUCESSFULLY #####")
    else:
        logging.info("##### DB ALREADY INITIALIZED #####")
