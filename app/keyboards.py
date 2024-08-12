from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='ОАОАОАОА')],
    [KeyboardButton(text='ЧЕГООООООО?!'), KeyboardButton(text='ТОГОООО!')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YT', url='https://youtube.com/@sudoteach')]
])




