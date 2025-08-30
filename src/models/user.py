from models.akonta import AkontaObject
from extras.enums import AccountTypeEnums
from peewee import *


class AkontaUser(AkontaObject):
    """
        Represente un utilisateur du systeme
        Un utilisateur peut etre un admin ou un vendeur
    """
    
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    username = CharField(max_length=20)
    email = CharField(max_length=50, null=True)
    phone = CharField(max_length=50)
    password = CharField(max_length=500)
    account_type = CharField(max_length=10, choices=AccountTypeEnums.items(), default=AccountTypeEnums.SELLER.value)
    last_seen = DateTimeField(null=True)


    def __str__(self):
        
        return f"{self.first_name} {self.last_name}"
    
    



