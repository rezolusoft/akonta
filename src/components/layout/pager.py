import flet as ft
from pages import dashboard
from components import side_menu, top_bar


def pager(page, content)->ft.Control:


    pager = ft.SafeArea(
            content = ft.Column(
                expand=True,
                controls=[
                    ft.Row(expand=True,
                        controls=[
                        
                        side_menu(page=page),
                        ft.Column(
                            controls=[
                                top_bar,
                                ft.Container(content=content, expand=True)
                            ],
                            expand=True
                            
                            ),
                       ])
                ],
            ),
            expand=True
        )
    return pager


