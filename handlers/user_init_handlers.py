from typing import Type

import telebot.types
from sqlalchemy.orm import Session

import db
from api.api_interaction import get_departments_dict, get_streams_dict, get_groups_dict
from bot import ASYNC_BOT
from decorators import should_be_registered
from utils.keyboard_utils import make_inline_keyboard


bot = ASYNC_BOT


async def handle_user_init(callback: telebot.types.CallbackQuery, init_user_callback_type: str, param: str):
    if init_user_callback_type == 'type':
        await handle_user_init_type(callback, user_type=param)
    elif init_user_callback_type == 'department':
        await handle_user_init_department(callback, department_id=int(param))
    elif init_user_callback_type == 'stream':
        await handle_user_init_stream(callback, stream_id=int(param))
    elif init_user_callback_type == 'group':
        await handle_user_init_group(callback, group_id=int(param))


async def handle_user_init_type(callback: telebot.types.CallbackQuery, user_type: str):
    user_id = callback.from_user.id

    session = Session(bind=db.engine)

    if not session.query(db.User).filter(db.User.id == user_id).scalar():
        user = db.User(id=user_id, department_id=None, stream_id=None, group_id=None)

        session.add(user)
        session.commit()

    session.close()

    if user_type == 'student':
        buttons_dict = dict()

        for department_name, department_id in get_departments_dict().items():
            buttons_dict[department_name] = f'init_user#department#{department_id}'

        await bot.send_message(user_id,
                               '<b>Выберете свой факультет/институт: </b>',
                               parse_mode='HTML',
                               reply_markup=make_inline_keyboard(buttons_dict))


@should_be_registered
async def handle_user_init_department(callback: telebot.types.CallbackQuery, department_id: int):
    user_id = callback.from_user.id

    session = Session(bind=db.engine)

    session.query(db.User).filter(db.User.id == user_id).update({'department_id': department_id})

    session.commit()
    session.close()

    buttons_dict = dict()

    for stream_name, stream_id in get_streams_dict(department_id).items():
        buttons_dict[stream_name] = f'init_user#stream#{stream_id}'

    await bot.send_message(user_id,
                           '<b>Выберете свой поток: </b>',
                           parse_mode='HTML',
                           reply_markup=make_inline_keyboard(buttons_dict))


@should_be_registered
async def handle_user_init_stream(callback: telebot.types.CallbackQuery, stream_id: int):
    user_id = callback.from_user.id

    session = Session(bind=db.engine)

    user: Type[db.User] = session.query(db.User).filter(db.User.id == user_id).one()

    department_id = user.department_id

    session.query(db.User).filter(db.User.id == user_id).update({'stream_id': stream_id})
    session.commit()
    session.close()

    buttons_dict = dict()

    for group_name, group_id in get_groups_dict(department_id, stream_id).items():
        buttons_dict[group_name] = f'init_user#group#{group_id}'

    await bot.send_message(user_id,
                           '<b>Выберете свою группу: </b>',
                           parse_mode='HTML',
                           reply_markup=make_inline_keyboard(buttons_dict))


@should_be_registered
async def handle_user_init_group(callback: telebot.types.CallbackQuery, group_id: int):
    user_id = callback.from_user.id

    session = Session(bind=db.engine)

    user: Type[db.User] = session.query(db.User).filter(db.User.id == user_id).one()

    session.query(db.User).filter(db.User.id == user_id).update({'group_id': group_id})
    session.commit()

    await bot.send_message(user_id,
                           f'<b>Вы успешно зарегистрировались!</b>\n'
                           f'<i>Ваш идентификатор: </i>{user.id}\n'
                           f'<i>Идентификатор вашего факультета/института: </i>{user.department_id}\n'
                           f'<i>Идентификатор вашего потока: </i>{user.stream_id}\n'
                           f'<i>Идентификатор вашей группы:</i> {user.group_id}\n',
                           parse_mode='HTML')

    session.close()


