import flet as ft
from components import side_menu
from themes import light_theme, dark_theme
from components import top_bar


def main(page: ft.Page):


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
                    ft.Row(
                        controls=[
                                top_bar
                                ]
                        ),
                    ft.Row(
                        expand=True,
                        controls=[
                            side_menu,   
                            ft.Container(
                                content=ft.Text("Contenu Principal"), 
                                bgcolor=ft.Colors.WHITE, 
                                expand=True),
                                ]
                        )
                ],
            ),
            expand=True


        )
    )


ft.app(main)
