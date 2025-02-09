import flet as ft


def main(page: ft.Page):
    # Данные
    data = {"Иванов": 101, "Петров": 102, "Сидоров": 103}

    # Словарь для хранения чекбоксов
    checkboxes = {}

    # Функция для обработки нажатия кнопки
    def on_submit(e):
        selected_ids = [id for name, id in data.items() if checkboxes[name].value]
        print("Выбранные ID:", selected_ids)

    # Генерируем чекбоксы
    for name, id in data.items():
        checkboxes[name] = ft.Checkbox(label=name)
        page.add(checkboxes[name])

    # Добавляем кнопку
    submit_btn = ft.ElevatedButton(text="Отправить", on_click=on_submit)
    page.add(submit_btn)

    page.update()


# Запуск приложения
ft.app(target=main)