import telebot

from api.api_interaction import get_today_schedule, get_tomorrow_schedule, get_week_schedule
from bot import ASYNC_BOT
from decorators import should_be_registered
from utils import chat_utils
from utils.users_utils import get_user

bot = ASYNC_BOT


@should_be_registered
async def handle_user_schedule(callback: telebot.types.CallbackQuery, schedule_date):
    if schedule_date == 'today':
        await handle_user_schedule_today(callback)
    elif schedule_date == 'tomorrow':
        await handle_user_schedule_tomorrow(callback)
    elif schedule_date == 'week':
        await handle_user_schedule_week(callback)


@should_be_registered
async def handle_user_schedule_today(callback: telebot.types.CallbackQuery):
    user_id = callback.from_user.id

    user = get_user(user_id)

    schedule_list = get_today_schedule(user.group_id)

    await chat_utils.print_schedule_day(schedule_list, bot, user.id, 'Расписание на сегодня: ')


@should_be_registered
async def handle_user_schedule_tomorrow(callback: telebot.types.CallbackQuery):
    user_id = callback.from_user.id

    user = get_user(user_id)

    schedule_list = get_tomorrow_schedule(user.group_id)

    await chat_utils.print_schedule_day(schedule_list, bot, user.id, 'Расписание на завтра: ')


@should_be_registered
async def handle_user_schedule_week(callback: telebot.types.CallbackQuery):
    user_id = callback.from_user.id

    user = get_user(user_id)

    schedule_dict = get_week_schedule(user.group_id)

    for date, schedule_list in schedule_dict.items():
        await chat_utils.print_schedule_day(schedule_list, bot, user.id, f'Расписание на {date}: ')
