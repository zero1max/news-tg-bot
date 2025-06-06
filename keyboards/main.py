from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

categories = ["🌍 Jahon", "🏅 Sport", "🧬 Fan", "💼 Biznes"]

def category_keyboard():
    buttons = [[KeyboardButton(text=cat)] for cat in categories]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
