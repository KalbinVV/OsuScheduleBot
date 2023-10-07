import telebot.types


def make_inline_keyboard(buttons_dict: dict[str, str]) -> telebot.types.InlineKeyboardMarkup:
    keyboard = telebot.types.InlineKeyboardMarkup()

    for button_name, callback_data in buttons_dict.items():
        button = telebot.types.InlineKeyboardButton(button_name, callback_data=callback_data)

        keyboard.add(button)

    return keyboard


def make_reply_keyboard(buttons_list: list[str]) -> telebot.types.ReplyKeyboardMarkup:
    keyboard = telebot.types.ReplyKeyboardMarkup()

    for button_name in buttons_list:
        button = telebot.types.KeyboardButton(button_name)

        keyboard.add(button)

    return keyboard
