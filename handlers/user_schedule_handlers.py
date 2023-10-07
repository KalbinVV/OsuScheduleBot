import telebot

from bot import ASYNC_BOT
from decorators import should_be_registered

bot = ASYNC_BOT


@should_be_registered
async def handle_user_schedule(callback: telebot.types.CallbackQuery, schedule_date):
    if schedule_date == 'today':
        await handle_user_schedule_today(callback)


@should_be_registered
async def handle_user_schedule_today(callback: telebot.types.CallbackQuery):
    user_id = callback.from_user.id

    await bot.send_message(user_id, 'Расписание на сегодня: ')
