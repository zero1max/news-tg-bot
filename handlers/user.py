from aiogram import F
from aiogram.types import Message
from aiogram.filters import CommandStart
from datetime import datetime
#
from loader import router_user
from keyboards.main import category_keyboard
from database.news import get_news_by_category


@router_user.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Salom! Yangiliklar botiga xush kelibsiz.", reply_markup=category_keyboard())

@router_user.message(F.text.in_(["🌍 Jahon", "🏅 Sport", "🧬 Fan", "💼 Biznes"]))
async def category_handler(message: Message):
    category_map = {
        "🌍 Jahon": "world",
        "🏅 Sport": "sport",
        "🧬 Fan": "science",
        "💼 Biznes": "business"
    }
    category = category_map[message.text]  # type: ignore
    news_list = await get_news_by_category(category)

    if not news_list:
        await message.answer("Bu bo'limda yangiliklar mavjud emas.")
        return

    for news in news_list:
        created_at = news.get('created_at')
        if isinstance(created_at, datetime):
            created_at_str = created_at.strftime("%Y-%m-%d %H:%M")
        else:
            created_at_str = str(created_at)

        text = f"📰 <b>{news['title']}</b>\n\n{news['content']}\n\n📅 {created_at_str}"
        await message.bot.send_photo( # type: ignore
            chat_id=message.chat.id,
            photo=news['image_id'],
            caption=text,
            parse_mode="HTML"
        )
