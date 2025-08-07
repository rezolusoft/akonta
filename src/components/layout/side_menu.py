import flet as ft
from .partial import side_menu_button


def menu_title(_title: str) -> ft.Control:

    title = ft.Container(ft.Text(value=_title))
    title.margin = ft.margin.only(top=10)
    return title


logo = ft.Container(ft.Image(src="Logo.png"), height=50)



spacer = ft.Container()

spacer.margin = ft.margin.symmetric(vertical=10)

side_menu = ft.Container(
    bgcolor=ft.Colors.SURFACE,

    content=ft.Column(
        expand=True,
        controls=[
            logo,
            menu_title('Menu Principal'),
            side_menu_button(title="Dashboard", icon="DASHBOARD_ROUNDED"),
            side_menu_button(title="Mon Stock", icon="WAREHOUSE_ROUNDED"),
            side_menu_button(title="Mes Produits", icon="INVENTORY_ROUNDED"),
            side_menu_button(title="Ma Caisse", icon="WALLET_ROUNDED"),
            side_menu_button(title="Mes statistiques",
                             icon="BAR_CHART_ROUNDED"),
            spacer,
            menu_title("Centre d'aide"),
            side_menu_button(title="Donner un avis", icon="MODE_COMMENT"),
            side_menu_button(title="Support Client",
                             icon="SUPPORT_AGENT_ROUNDED"),

        ],



    )
)


side_menu.border_radius = ft.border_radius.all(7)
side_menu.padding = ft.padding.all(10)
