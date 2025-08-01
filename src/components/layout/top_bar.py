import flet as ft


logo = ft.Container(ft.Image(src="Logo.png"))
logo.padding = ft.padding.all(10)
logo.margin = ft.margin.only(left=10, right=5)


divider = ft.Container(ft.VerticalDivider(color=ft.Colors.ON_SURFACE))
divider.padding = ft.padding.symmetric(vertical=5)

top_bar = ft.Container(
                        bgcolor=ft.Colors.SURFACE, 
                        expand=True,
                        height=70,
                        content=ft.Row(controls=[
                            logo,
                            divider
                        ]), 
                        
                        )

top_bar.border_radius = ft.border_radius.all(10)


