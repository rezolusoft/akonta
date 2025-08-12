import flet as ft
from themes import light_theme, dark_theme
from components import pager, routes
from importlib import import_module


def main(page: ft.Page):


    # Maximiser la fenetre
    page.window.maximized = True
    # Definir Titre
    page.title = "Akonta"

    # Charger le theme
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = light_theme
    page.dark_theme = dark_theme
    page.bgcolor = page.theme.color_scheme.background

    # initialiser le contenu a vide
    content_container = ft.Container(expand=True)

    # initialisation de l'echaffaudage
    layout = pager(page=page, content=content_container)

    def router(e: ft.RouteChangeEvent):
        # charger dynamiquement le contenu
        # adequat en fonction de la route
        route = page.route

        if route in routes:
            route = route.lstrip("/")
            content = import_module(f"pages.{route}")
            content_container.content = getattr(content, route)()
        else:
            content_container.content = ft.Text("Page introuvable")
        # reconstruire l'echaffaudage au changement de route 
        layout.content = pager(page=page, content=content_container)
        page.update()


                


    # ajout de l'echaffaudage a la page
    page.add(layout)

    page.on_route_change = router

    # Controle de la page par défaut
    if page.route == "/":
        page.go('/dashboard')
    else:
        page.go(page.route)

ft.app(main)
