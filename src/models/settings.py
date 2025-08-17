from models.akonta import AkontaObject
from extras.enums import CurrencyTypeEnums
from peewee import *


class AkontaSetting(AkontaObject):
    config_name = CharField(default="default")
    default_currency = DecimalField(choices=CurrencyTypeEnums.items())
    editable_price = BooleanField(default=False)



