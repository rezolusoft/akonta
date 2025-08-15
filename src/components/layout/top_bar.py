import flet as ft
from components.partial import top_bar_title, search_bar, settings_menu


top_bar = ft.Container(
    bgcolor=ft.Colors.SURFACE,

    content=ft.Row(controls=[
        
        top_bar_title('Dashboard', 'Bon retour sur Akonta'),
        
        search_bar(), 

        settings_menu()

    ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

)

top_bar.border_radius = ft.border_radius.all(7)
