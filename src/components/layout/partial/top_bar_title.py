import flet as ft

def top_bar_title(_title:str, description:str)->ft.Control:

    title = ft.Container(
        ft.Column(
        controls=[
            ft.Text(_title, size=20, weight=ft.FontWeight.BOLD),
            ft.Text(description)
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER
    )
    )
    title.margin = ft.margin.symmetric(vertical=5)
    return title

