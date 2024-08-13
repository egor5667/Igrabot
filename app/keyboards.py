from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# main = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
#     [InlineKeyboardButton(text='Корзина', callback_data='basket'),
#      InlineKeyboardButton(text='Контакты', callback_data='contact')]])

# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='YT', url='https://youtube.com/@sudoteach')]
# ])


faculty_one = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Естественно-технологический факультет', callback_data='et')],
    [InlineKeyboardButton(text='Высшая шк. физической культуры и спорта', callback_data='sport')],
    [InlineKeyboardButton(text='Исторический факультет', callback_data='ist')],
    [InlineKeyboardButton(text='Факультет дошкольного образования', callback_data='doshfak')],
    [InlineKeyboardButton(text=':right: Далее', callback_data='1to2')]
])

faculty_two = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Факультет инклюзивного и коррекц. образования', callback_data='fiko')],
    [InlineKeyboardButton(text='Факультет иностранных языков', callback_data='inyaz')],
    [InlineKeyboardButton(text='Факультет математики, физики и информатики', callback_data='mfi')],
    [InlineKeyboardButton(text='Факультет подгот. учителей начальных классов', callback_data='unk')],
    [InlineKeyboardButton(text='след. страница', callback_data='2to3')],
    [InlineKeyboardButton(text='Пред. страница', callback_data='2to1')]
])

faculty_three = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Филологический факультет', callback_data='filfak')],
    [InlineKeyboardButton(text='Колледж', callback_data='colege')],
    [InlineKeyboardButton(text='Факультет психологии', callback_data='psifak')],
    [InlineKeyboardButton(text='Профессионально-педагогический институт', callback_data='ppi')],
    [InlineKeyboardButton(text='Пред. страница', callback_data='3to2')]
])


