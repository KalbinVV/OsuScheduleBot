from telebot.async_telebot import AsyncTeleBot

from api.schedule_record import ScheduleRecord


async def print_schedule_day(schedule_list: list[ScheduleRecord], bot: AsyncTeleBot, chat_id: int,
                             title: str) -> None:
    result_string = f'<b>{title}</b>\n\n'

    if len(schedule_list) == 0:
        result_string += 'На этот день нет пар!'

    for schedule_record in schedule_list:
        result_string += f'<b>{schedule_record.class_id} пара:</b>\n' \
                         f'{schedule_record.class_name}\n' \
                         f'{schedule_record.class_room}\n' \
                         f'{schedule_record.teacher_name}\n\n'

    await bot.send_message(chat_id, result_string, parse_mode='HTML')
