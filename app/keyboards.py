from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# main = ReplyKeyboardMarkup(inline_keyboard=[
#     [KeyboardButton(text='Каталог', callback_data='catalog')],
#     [KeyboardButton(text='Корзина', callback_data='basket'),
#      KeyboardButton(text='Контакты', callback_data='contact')]])

# settings = ReplyKeyboardMarkup(inline_keyboard=[
#     [KeyboardButton(text='YT', url='https://youtube.com/@sudoteach')]
# ])


faculty_one = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Естественно-технологический факультет')],
    [KeyboardButton(text='Высшая шк. физической культуры и спорта')],
    [KeyboardButton(text='Исторический факультет')],
    [KeyboardButton(text='Факультет дошкольного образования')],
    [KeyboardButton(text='➡️На стр. 2')]
])

faculty_two = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Факультет инклюзивного и коррекц. образования')],
    [KeyboardButton(text='Факультет иностранных языков')],
    [KeyboardButton(text='Факультет математики, физики и информатики')],
    [KeyboardButton(text='Факультет подгот. учителей начальных классов')],
    [KeyboardButton(text='➡️На стр. 3')],
    [KeyboardButton(text='⬅️На стр. 1')]
])

faculty_three = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Филологический факультет')],
    [KeyboardButton(text='Колледж')],
    [KeyboardButton(text='Факультет психологии')],
    [KeyboardButton(text='Профессионально-педагогический институт')],
    [KeyboardButton(text='⬅️На стр. 2')]
])

YNkeyb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='✅Да'), KeyboardButton(text='❌Нет')]
])

base_key = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text='СЖЕЕЕЧЬ ВСЁЁЁЁ!!!!!')]
])


class KeyAdm:
    menuKey = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Встречи')],
        [KeyboardButton(text='Создать рассылку')]
    ])
    meetKey = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Начать встречу')],
        [KeyboardButton(text='Завершить встречу')]
    ])
    sendKey = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton(text='Завершить создание рассылки')],
        [KeyboardButton(text='Редактировать текст')]
    ])

