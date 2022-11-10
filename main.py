# import sqlite3
# import telebot
import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN

loop = asyncio.new_event_loop()
bot = Bot(TOKEN, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher(bot, loop=loop, storage=storage)

async def shutdown(dp):
    await storage.close()
    await bot.close()

if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=shutdown)

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id,
#                      'Добрый день! Этот опрос посвящен определению интересов нашей аудитории с целью увеличения ассортимента нашего интернет магазина открыток. Пожалуйста, ответьте на 8 вопросов:')
#
#
# conn = sqlite3.connect('db/database.db', check_same_thread=False)
# cursor = conn.cursor()
#
#
# def db_table_val(user_id: int, sex: bool, age: int, website: bool, sending: int, envelope: bool, decor: int,
#                  abroad: bool):
#     cursor.execute(
#         'INSERT INTO users (user_id, sex, age, website, sending, envelope, decor, abroad) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
#         (user_id, sex, age, website, sending, envelope, decor, abroad))
#     conn.commit()
#
#
# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.from_user.id, 'Привет! Ваше имя добавленно в базу данных!')
#     user_id = message.from_user.id
#     db_table_val(user_id=user_id, sex='true', age=1, website='true', sending=2, envelope='true', decor=1,
#                  abroad='false')
#
#
#
