import telebot.types

from bot import ASYNC_BOT
from decorators import should_be_registered
from utils.keyboard_utils import make_inline_keyboard
from utils.users_utils import get_user

bot = ASYNC_BOT


@should_be_registered
async def handle_user_information_button(message: telebot.types.Message):
    user_id = message.chat.id

    user = get_user(user_id)

    await bot.send_message(user_id,
                           f'<b>Разработчик:</b> Владимир Кальбин\n'
                           f'<b>Версия:</b> 0.1\n\n'
                           f'<b>Ваши данные:</b>\n'
                           f'<i>Ваш идентификатор: </i>{user.id}\n'
                           f'<i>Идентификатор вашего факультета/института: </i>{user.department_id}\n'
                           f'<i>Идентификатор вашего потока: </i>{user.stream_id}\n'
                           f'<i>Идентификатор вашей группы:</i> {user.group_id}\n',
                           parse_mode='HTML')


@should_be_registered
async def handle_user_schedule_button(message: telebot.types.Message):
    user_id = message.chat.id

    inline_keyboard = make_inline_keyboard({
        'Сегодня': 'schedule#today',
        'Завтра': 'schedule#tomorrow',
        'На неделю': 'schedule#week'
    })

    await bot.send_message(user_id,
                           '<b>Выберете расписание из предложенных вариантов:</b>',
                           parse_mode='HTML',
                           reply_markup=inline_keyboard)



