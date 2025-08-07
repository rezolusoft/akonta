import flet as ft
from components import side_menu
from themes import light_theme, dark_theme
from components import top_bar
from pages import dashboard


def main(page: ft.Page):


    page.window.maximized = True
    page.title = "Akonta"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = light_theme
    page.dark_theme = dark_theme
    page.bgcolor = page.theme.color_scheme.background

    page.add(
        ft.SafeArea(
            content = ft.Column(
                expand=True,
                controls=[
                    ft.Row(expand=True,
                        controls=[
                        
                        side_menu,
                        ft.Column(
                            controls=[
                                top_bar,
                                 dashboard
                            ],
                            expand=True
                            
                            ),
                        

                       ])
                ],
            ),
            expand=True
        )
    )


ft.app(main)
