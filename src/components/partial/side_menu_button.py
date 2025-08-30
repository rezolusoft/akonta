import flet as ft

def side_menu_button(title, icon, page=None, destination=None)->ft.Control:

    # Déterminer si ce bouton est actif
    is_active = (page.route == destination)

    # Couleurs
    default_bg = ft.Colors.TRANSPARENT
    hover_bg = ft.Colors.ORANGE_50
    active_bg = ft.Colors.ORANGE_100

    # On part avec la couleur active ou par défaut
    bg_color = active_bg if is_active else default_bg

    button = ft.Container(
                ft.Row(
                    controls=[
                        ft.Icon(name=icon, color=ft.Colors.PRIMARY),
                        ft.Text(title),
                    
                    ],
                  expand=True,  
                ),
                padding=ft.padding.all(10),
                bgcolor=bg_color,
                on_click= lambda e : page.go(destination),
                border_radius=ft.border_radius.all(5),

                
            )
    
    def on_hover(e: ft.HoverEvent):
        if not is_active:  # On ne change pas si déjà actif
            button.bgcolor = hover_bg if e.data == "true" else default_bg
            button.update()

    button.on_hover = on_hover
    
    return button
