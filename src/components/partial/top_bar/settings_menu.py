import flet as ft
from .top_bar_title import top_bar_title
from .avatar import avatar


def settings_menu() -> ft.Control:

    menu = ft.Container(
        ft.Row(
        controls=[
            avatar(),   
            top_bar_title("Rezolusoft", "Votre compte", 16)
          ],
    ),
    margin=ft.margin.only(right=15),)

    return menu
