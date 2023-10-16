import datetime

import telebot

from api.api_interaction import get_today_schedule, get_tomorrow_schedule, get_week_schedule, get_schedule_at
from bot import ASYNC_BOT
from decorators import should_be_registered
from utils import chat_utils
from utils.format_utils import format_weekday_to_string
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
    else:
        await handle_user_schedule_at(callback)


@should_be_registered
async def handle_user_schedule_today(callback: telebot.types.CallbackQuery):
    user_id = callback.from_user.id

    user = get_user(user_id)

    schedule_list = get_today_schedule(user.group_id)

    today_day = datetime.datetime.now()
    today_day_str = today_day.strftime('%d.%m.20%y')

    weekday = format_weekday_to_string(today_day.isoweekday())

    await chat_utils.print_schedule_day(schedule_list, bot, user.id, f'Расписание на сегодня ({weekday}): ',
                                        enable_keyboard=True,
                                        date_str=today_day_str)


@should_be_registered
async def handle_user_schedule_tomorrow(callback: telebot.types.CallbackQuery):
    user_id = callback.from_user.id

    user = get_user(user_id)

    schedule_list = get_tomorrow_schedule(user.group_id)

    tomorrow_day = datetime.datetime.now() + datetime.timedelta(days=1)

    tomorrow_day_str = tomorrow_day.strftime('%d.%m.20%y')

    weekday = format_weekday_to_string(tomorrow_day.isoweekday())

    await chat_utils.print_schedule_day(schedule_list, bot, user.id, f'Расписание на завтра ({weekday}): ',
                                        enable_keyboard=True,
                                        date_str=tomorrow_day_str)


@should_be_registered
async def handle_user_schedule_week(callback: telebot.types.CallbackQuery):
    user_id = callback.from_user.id

    user = get_user(user_id)

    schedule_dict = get_week_schedule(user.group_id)

    for date, schedule_list in schedule_dict.items():
        date_obj = datetime.datetime.strptime(date, '%d.%m.20%y')
        weekday = format_weekday_to_string(date_obj.isoweekday())

        await chat_utils.print_schedule_day(schedule_list, bot, user.id, f'Расписание на {date} ({weekday}): ')


async def handle_user_schedule_at(callback: telebot.types.CallbackQuery):
    date = callback.data.split('#')[1]

    # TODO: Улучшить этот код:
    date_obj = datetime.datetime.strptime(date, '%d.%m.20%y')

    date_str = date_obj.strftime('%d.%m.20%y')

    weekday = format_weekday_to_string(date_obj.isoweekday())

    user = get_user(callback.from_user.id)

    schedule_list = get_schedule_at(user.group_id, date)

    await chat_utils.print_schedule_day(schedule_list, bot, user.id,
                                        f'Расписание на {date} ({weekday}) : ',
                                        enable_keyboard=True,
                                        date_str=date_str)
