import flet as ft
from components.layout import side_menu, top_bar


def pager(page, content)->ft.Control:


    pager = ft.Container(
                content=ft.Column(
                    expand=True,
                    controls=[
                        ft.Row(expand=True,
                            controls=[
                            
                            side_menu(page=page),
                            ft.Column(
                                controls=[
                                    top_bar(),
                                    ft.Container(content=content, expand=True)
                                ],
                                expand=True
                                
                                ),
                           ])
                    ],
                ),
                # image=ft.DecorationImage("img/3.jpg", fit=ft.ImageFit.COVER),
                expand=True,
                border_radius=ft.border_radius.all(5),
                padding=ft.padding.all(5),
                # bgcolor=page.theme.color_scheme.background
            )
    return pager


