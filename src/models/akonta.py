from datetime import datetime
from models import db
from peewee import *

# initialiser la base de donnée



class AkontaObject(Model):
    """
        Objet Akonta est le model de base dont heritera tous les models
        de la base de données. Il porte comme attribut les attributs communs
        à tous nos objets.
    """
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(null=True)
    deleted = BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.id is not None:
            self.updated_at=datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        database = db

