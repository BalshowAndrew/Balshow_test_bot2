from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import logging

from config import TOKEN
import keyboards

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id, 'Hello\!', reply_markup=keyboards.keyboard_start)


@dp.message_handler(Text(equals='Нажми на кнопку'))
async def cmd_info(message: types.Message):
    await bot.send_message(message.chat.id, 'Для разработчиков на языке *Python*', reply_markup=keyboards.keyboard_info)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
