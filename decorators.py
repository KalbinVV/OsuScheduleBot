import telebot.types
import bot
from utils.users_utils import user_exists


def should_be_registered(func):
    async def wrapper(*args, **kwargs):
        if isinstance(args[0], telebot.types.Message):
            message: telebot.types.Message = args[0]
            user_id = message.from_user.id
        elif isinstance(args[0], telebot.types.CallbackQuery):
            callback: telebot.types.Message = args[0]
            user_id = callback.from_user.id
        else:
            raise Exception(f'Неизвестный аргумент для декоратора "should_be_registered": {type(args[0])}')

        if not user_exists(user_id):
            await bot.ASYNC_BOT.send_message(user_id,
                                             '<b>Вы должны быть зарегистрированы, '
                                             'перед тем как пользоваться данной командой!</b>\n'
                                             '<i>Нажмите на клавиатуре "Сброс", либо вручную введите /start</i>',
                                             parse_mode='HTML')
        else:
            await func(*args, **kwargs)

    return wrapper
