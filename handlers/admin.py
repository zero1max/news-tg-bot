from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
#
from loader import router_admin
from middlewares.admin_filter import AdminFilter
from keyboards.admin import admin_main, category_inline, delete_news_inline
from database.db import news_collection
from datetime import datetime
from bson.objectid import ObjectId


router_admin.message.filter(AdminFilter())  

class NewsStates(StatesGroup):
    category = State()
    title = State()
    content = State()
    image = State()

@router_admin.message(CommandStart())
async def admin_start(message: Message):
    await message.answer("Admin panelga xush kelibsiz!", reply_markup=admin_main)

@router_admin.message(F.text == "➕ News qo‘shish")
async def add_news_start(message: Message, state: FSMContext):
    await message.answer("Kategoriya tanlang:", reply_markup=category_inline())
    await state.set_state(NewsStates.category)

@router_admin.callback_query(F.data.startswith("cat_"))
async def category_selected(callback: CallbackQuery, state: FSMContext):
    category = callback.data.split("_")[1] # type: ignore
    await state.update_data(category=category)
    await callback.message.answer("Sarlavhani kiriting:") # type: ignore
    await state.set_state(NewsStates.title)
    await callback.answer()

@router_admin.message(NewsStates.title)
async def get_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Yangilik matnini kiriting:")
    await state.set_state(NewsStates.content)

@router_admin.message(NewsStates.content)
async def get_content(message: Message, state: FSMContext):
    await state.update_data(content=message.text)
    await message.answer("Iltimos, yangilik rasmi (image) yuboring:")
    await state.set_state(NewsStates.image)

@router_admin.message(NewsStates.image, F.photo)
async def get_image(message: Message, state: FSMContext):
    data = await state.get_data()
    photo_id = message.photo[-1].file_id # type: ignore

    news = {
        "title": data['title'],
        "content": data['content'],
        "category": data['category'],
        "image_id": photo_id,
        "created_at": datetime.utcnow()
    }

    await news_collection.insert_one(news)
    await message.answer("✅ Yangilik muvaffaqiyatli qo‘shildi!", reply_markup=admin_main)
    await state.clear()

# ------------------------------- View News ---------------------------------------

@router_admin.message(F.text == "📋 News ko‘rish")
async def view_news(message: Message):
    news_cursor = news_collection.find().sort("created_at", -1).limit(5)
    news_list = [news async for news in news_cursor]

    if not news_list:
        await message.answer("📭 Hech qanday yangilik topilmadi.")
        return

    for news in news_list:
        created_at = news.get("created_at")
        created_at_str = created_at.strftime("%Y-%m-%d %H:%M") if created_at else "Nomaʼlum vaqt"

        text = f"📰 <b>{news['title']}</b>\n\n{news['content']}\n\n📂 Kategoriya: {news['category']}\n📅 {created_at_str}"
        await message.bot.send_photo( # type: ignore
            chat_id=message.chat.id,
            photo=news['image_id'],
            caption=text,
            parse_mode="HTML"
        )

# ------------------------------- Delete News -----------------------------------------------

@router_admin.message(F.text == "🗑 News o‘chirish")
async def delete_news_menu(message: Message):
    news_cursor = news_collection.find().sort("created_at", -1).limit(5)
    news_list = [news async for news in news_cursor]

    if not news_list:
        await message.answer("🗑 O‘chirish uchun yangilik yo‘q.")
        return

    await message.answer("O‘chirish uchun yangilikni tanlang:", reply_markup=delete_news_inline(news_list))

@router_admin.callback_query(F.data.startswith("del_"))
async def delete_selected_news(callback: CallbackQuery):
    news_id = callback.data.split("_")[1] # type: ignore
    try:
        result = await news_collection.delete_one({"_id": ObjectId(news_id)})
        if result.deleted_count == 1:
            await callback.message.answer("✅ Yangilik o‘chirildi.") # type: ignore
        else:
            await callback.message.answer("⚠️ Yangilik topilmadi.") # type: ignore
    except Exception as e:
        await callback.message.answer("❌ O‘chirishda xatolik yuz berdi.") # type: ignore
    await callback.answer()
