import asyncio

import telebot.types

from bot import ASYNC_BOT
from db import init_db
from handlers.user_buttons_handlers import handle_user_information_button, handle_user_schedule_button
from handlers.user_init_handlers import handle_user_init
from handlers.user_schedule_handlers import handle_user_schedule
from utils.keyboard_utils import make_inline_keyboard, make_reply_keyboard

bot = ASYNC_BOT


@bot.message_handler(commands=['start'])
async def init_user(message: telebot.types.Message):
    inline_keyboard = make_inline_keyboard({"Я студент 🧑‍🎓": "init_user#type#student"})

    keyboard = make_reply_keyboard(['Расписание 📆', 'Информация ℹ️', 'Сброс 🔄'])

    await bot.send_message(message.chat.id, '<b> Добро пожаловать в бот для расписаний ОГУ!</b>',
                           parse_mode='HTML',
                           reply_markup=keyboard)

    await bot.send_message(message.chat.id,
                           "<b>Перед началом работы, создайте аккаунт:</b>",
                           parse_mode='HTML',
                           reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: True)
async def handle_query(callback: telebot.types.CallbackQuery):
    args = callback.data.split('#')

    callback_type = args[0]

    if callback_type == 'init_user':
        init_user_callback_type = args[1]
        param = args[2]

        await handle_user_init(callback, init_user_callback_type, param)
    elif callback_type == 'schedule':
        schedule_date = args[1]

        await handle_user_schedule(callback, schedule_date)


@bot.message_handler(func=lambda message: True)
async def handle_text_messages(message: telebot.types.Message):
    if message.text == 'Сброс 🔄':
        await init_user(message)
    elif message.text == 'Информация ℹ️':
        await handle_user_information_button(message)
    elif message.text == 'Расписание 📆':
        await handle_user_schedule_button(message)


def main():
    init_db()

    asyncio.run(bot.polling())


if __name__ == '__main__':
    main()
    