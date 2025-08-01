import flet as ft
from .partial.top_bar_title import top_bar_title


logo = ft.Container(ft.Image(src="Logo.png"))
logo.padding = ft.padding.all(15)
logo.margin = ft.margin.only(left=10, right=10)



top_bar = ft.Container(
                        bgcolor=ft.Colors.SURFACE, 
                        expand=True,
                        height=70,
                        content=ft.Row(controls=[
                            ft.Row(
                                controls=[
                                    logo,
                                    top_bar_title('Dashboard', 'Bienvenue, Rezolusoft')
                                ]
                            ),
                            
                            
                        ]), 
                        
                        )

top_bar.border_radius = ft.border_radius.all(10)


