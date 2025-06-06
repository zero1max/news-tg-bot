from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

admin_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ News qo‘shish")],
        [KeyboardButton(text="🗑 News o‘chirish")],
        [KeyboardButton(text="📋 News ko‘rish")],
    ],
    resize_keyboard=True
)

def category_inline():
    buttons = [
        [InlineKeyboardButton(text="🌍 Jahon", callback_data="cat_world")],
        [InlineKeyboardButton(text="🏅 Sport", callback_data="cat_sport")],
        [InlineKeyboardButton(text="🧬 Fan", callback_data="cat_science")],
        [InlineKeyboardButton(text="💼 Biznes", callback_data="cat_business")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def delete_news_inline(news_list):
    builder = InlineKeyboardBuilder()
    for news in news_list:
        builder.button(
            text=news["title"][:30], 
            callback_data=f"del_{str(news['_id'])}"
        )
    return builder.as_markup()