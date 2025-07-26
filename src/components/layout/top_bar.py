import flet as ft
top_bar = ft.Container(
                        content=ft.Text("Barre d'action horizontale"), 
                        bgcolor=ft.Colors.WHITE, 
                        expand=True,
                        height=60)

top_bar.border_radius = ft.border_radius.all(10)