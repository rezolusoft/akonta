import flet as ft
from .side_menu_button import side_menu_button


side_menu = ft.Container(
    bgcolor=ft.Colors.WHITE,
    expand_loose=True,
    
    content=ft.Column(
        expand_loose=True,
        controls=[

            side_menu_button(title="Tableau de Board", icon="DASHBOARD_ROUNDED"),
            side_menu_button(title="Mon Stock", icon="WAREHOUSE_ROUNDED"),
            side_menu_button(title="Mes Produits", icon="INVENTORY_ROUNDED"),
            side_menu_button(title="Ma Caisse", icon="WALLET_ROUNDED"),
            side_menu_button(title="Mes statistiques", icon="BAR_CHART_ROUNDED")
           
        ],
        


    )
)


side_menu.border_radius = ft.border_radius.all(10)
side_menu.padding = ft.padding.all(20)

