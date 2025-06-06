import os
from aiogram import Dispatcher , Router, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
ADMIN_IDS = ["Admin_ID"] 

dp = Dispatcher()
router_admin = Router()
router_user = Router()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)) # type: ignore
dp.include_router(router=router_admin)
dp.include_router(router=router_user)