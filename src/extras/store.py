class AkontaStore():
    """
    Store
    Classe permettant de gerer le stockage de données utilisateur
    produite et exploitée par l'application

    liste des donnees: \n
    db_init -> permet de stocker l'etat de la bd

    """
    prefix = "akonta"

    def __init__(self, page):
        self.page = page
    
    def set(self, key, data):
        key = f"{self.prefix}_{key}"
        self.page.client_storage.set(key, data)

    def get(self, key):
        key = f"{self.prefix}_{key}"
        return self.page.client_storage.get(key)