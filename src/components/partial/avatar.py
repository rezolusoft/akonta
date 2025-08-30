import flet as ft


def avatar()->ft.Control:

    avatar =    ft.Container(
                ft.Stack(
                    [
                        ft.Container(
                            ft.Image("img/cube.png"),

                            padding=ft.padding.all(0),
                            border_radius=ft.border_radius.all(30),

                            shadow=ft.BoxShadow(
                                spread_radius=0.5,
                                blur_radius=5,
                                color=ft.Colors.ON_SURFACE,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            )

                        ),
                        ft.Container(
                            content=ft.Text("1", color=ft.Colors.WHITE),
                            alignment=ft.alignment.center,

                            border_radius=ft.border_radius.all(9),
                            bgcolor=ft.Colors.RED,
                            top=-0,
                            right=-0,
                            width=18,
                            height=18
                        ),

                    ]
                ),

                width=60,
                height=60,
                padding=ft.padding.only(left=5, right=0, top=5, bottom=5),
                margin=ft.margin.only(left=10, top=5, bottom=5, right=0)


            )
    return avatar
