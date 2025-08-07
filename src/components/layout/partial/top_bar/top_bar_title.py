import flet as ft

def top_bar_title(_title:str, description:str, size=20)->ft.Control:

    title = ft.Container(
        ft.Column(
        controls=[
            ft.Text(_title, size=size, weight=ft.FontWeight.BOLD),
            ft.Text(description)
        ],
        spacing=0,
        alignment=ft.MainAxisAlignment.CENTER
        
    )
    )
    if size==20:
        # hack pour controler le rendu de la marge
        # le text est plus petit que 20 au niveau 
        # des boutton etc..
        title.margin = ft.margin.all(10)

    return title


