from aiogram import types

# кнопка-шаблон для команды /start
buttons_start = ['Нажми на кнопку']
keyboard_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_start.add(*buttons_start)


# inline-кнопки для перехода на сайт и телеграм канал
buttons_info = [
    types.InlineKeyboardButton(text='*Информация*', url='https://docs.python.org/3.10/tutorial/index.html'),
    types.InlineKeyboardButton(text='*Список литературы*', url='https://t.me/pythonlbooks')
    ]
keyboard_info = types.InlineKeyboardMarkup(row_width=1)
keyboard_info.add(*buttons_info)