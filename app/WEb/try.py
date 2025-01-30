import flet as ft
from flet.core.icons import icons


def main(page: ft.Page):

    userLabel = ft.Text('Info')
    userText = ft.TextField(value="0", width=150, text_align=ft.TextAlign.CENTER)

    def get_info(e):
        userLabel.value = userText.value
        page.update()


    page.title = "Приложение"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.HOME, on_click=get_info),
                ft.Icon(ft.icons.BACK_HAND)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
            userLabel,
            userText
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
