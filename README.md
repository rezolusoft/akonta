# Akonta 📦  
**Simple, powerful inventory management software for small businesses and retail stores.**  


##Organisation du Repo

- ```/src/components``` : Repertoire principal qui comporte l'ensemble des 
controles presonalisés

- ```/src/components/layout``` : Contient les controles dynamiques de l'echaffaudage de l'application notament : un pager qui met en place la structure de base en chargeant en son sein la ```side_menu``` et la ```top_bar```. Il contient egalement un fichier routes qui liste l'ensemble des routes liés à chaque pages dans src/pages.

- ```/src/pages``` : contient l'ensemble des pages des l'application. Les pages sont intresquement liées aux routes listé dans ```src/components/layout/routes```. Chaque route correspond à un fichier dans ```/src/page``` au nom de cette route qui porte en son sein une fonction du meme nom censé retourner un objet flet.Control representant le contenu de la page
```python 
    # Exemple
    # -------

    # src/component/layout/routes.py
    routes = [..., 'dashboard', '...']


    # src/pages/dashboard.py
    def dashboard()->flet.Control:
        return flet.Container()
    
```

- ```/src/models``` : contient les fichier de gestion des données de la bd

- ```/src/themes``` : contient les fichiers de themes

- ```/src/assets``` : contient les assets





