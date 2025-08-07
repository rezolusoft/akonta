import flet as ft

def side_menu_button(title, icon, destination=None)->ft.Control:

    button = ft.Container(
                ft.Row(
                    controls=[
                        ft.Icon(name=icon,
                                color=ft.Colors.PRIMARY),
                        ft.Text(title)
                    ],
                ),
                padding=ft.padding.all(10)


            )
    
    return button
