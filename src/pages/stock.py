import flet as ft

def stock()->ft.Control :
    stock = ft.Container(content=ft.Text("Stock -> Contenu Principal"), bgcolor=ft.Colors.SURFACE)
    return stock
