import flet as ft
from DBcontrol import GetData, Achives

def main(page: ft.Page):
    page.title = "Администрирвание"
    page.bgcolor = ft.colors.WHITE
    page.scroll = 'adaptive'

    def create_home_view():
        return ft.View(
            "/",
            [
                ft.AppBar(
                    title=ft.Text("Меню", size=24, weight=ft.FontWeight.BOLD),
                    bgcolor=ft.colors.BLUE_600,
                    color=ft.colors.WHITE
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Выберите действие", size=20, weight=ft.FontWeight.NORMAL),
                            ft.ElevatedButton(
                                "Коины",
                                on_click=lambda _: page.go("/coins")
                            ),
                            ft.ElevatedButton(
                                text='Рассылки',
                                on_click=lambda _: page.go("/sends")
                            ),
                            ft.ElevatedButton(
                                text='Встречи',
                                on_click=lambda _: page.go("/meets")
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=26
                    ),
                    padding=20,
                    alignment=ft.alignment.center,
                ),
            ],
        )

    def create_coin_view():
        return ft.View(
            "/coins",
            [
                ft.AppBar(
                    leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/"),),
                    title=ft.Text("Коины", size=24, weight=ft.FontWeight.BOLD),
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Управление начислением", size=20, weight=ft.FontWeight.NORMAL),
                            ft.ElevatedButton(
                                "Вернуться на главную",
                                on_click=lambda _: page.go("/"),
                                bgcolor=ft.colors.BLUE_500,
                                color=ft.colors.WHITE,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=20,
                    alignment=ft.alignment.center,
                ),
            ],
        )
    def create_meets_view():
        data = GetData.GetUserIds()
        checks = {}
        def on_submit(e):
            selected_ids = [id for name, id in data.items() if checks[name].value]
            print("Выбранные ID:", selected_ids)
            for i in range(len(selected_ids)):
                Achives.coinUpdater(selected_ids[i], 15)
        sub_btn = ft.ElevatedButton(text="Отправить", on_click=on_submit)
        meet_cont = [
            ft.Text(value="Отметки на встречах", size=20, weight=ft.FontWeight.NORMAL)
            ]
        for name, id in data.items():
            checks[name] = ft.Checkbox(label=name)
            meet_cont.append(checks[name])
        meet_cont.append(sub_btn)
        meet_cont.append(ft.ElevatedButton(text="Вернуться на лавную", on_click=lambda _: page.go("/")))
        return ft.View(
            route="/meets",
            controls=[
                ft.AppBar(
                    leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/"),),
                    title=ft.Text("Встречи", size=24, weight=ft.FontWeight.BOLD),
                ),
                ft.Column(
                    controls=meet_cont, scroll='adaptive', height=600,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
            ], padding=20
        )

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        if page.route == "/":
            page.views.append(create_home_view())
        elif page.route == "/coins":
            page.views.append(create_coin_view())
        elif page.route == "/meets":
            page.views.append(create_meets_view())
        page.update()


    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)