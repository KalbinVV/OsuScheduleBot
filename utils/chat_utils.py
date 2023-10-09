import datetime

from telebot.async_telebot import AsyncTeleBot

from api.schedule_record import ScheduleRecord
from utils.keyboard_utils import make_inline_keyboard


async def print_schedule_day(schedule_list: list[ScheduleRecord], bot: AsyncTeleBot, chat_id: int,
                             title: str,
                             enable_keyboard: bool = False,
                             date_str: str = '') -> None:
    # TODO: улучшить эту часть кода
    timetable_of_classes = {1: '08:00-09:30',
                            2: '09:40-11:10',
                            3: '11:20-12:50',
                            4: '13:20-14:50',
                            5: '15:00-16:30',
                            6: '16:40 - 18:10',
                            7: '18:20 - 19:50',
                            8: '20:00 - 21:30'}

    result_string = f'<b>{title}</b>\n\n'

    if len(schedule_list) == 0:
        result_string += 'На этот день нет пар!'

    for schedule_record in schedule_list:
        class_id = schedule_record.class_id

        result_string += f'<b>{class_id} пара ({timetable_of_classes[class_id]}): </b>\n' \
                         f'{schedule_record.class_name}\n' \
                         f'{schedule_record.class_room}\n' \
                         f'{schedule_record.teacher_name}\n\n'

    if enable_keyboard:
        next_day_obj = datetime.datetime.strptime(date_str, '%d.%m.20%y') + datetime.timedelta(days=1)
        next_day_str = next_day_obj.strftime('%d.%m.20%y')

        inline_keyboard = make_inline_keyboard({'Расписание на следующий день': f'schedule#{next_day_str}'})

        await bot.send_message(chat_id, result_string, parse_mode='HTML', reply_markup=inline_keyboard)
    else:
        await bot.send_message(chat_id, result_string, parse_mode='HTML')
