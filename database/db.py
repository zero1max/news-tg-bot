from motor.motor_asyncio import AsyncIOMotorClient
from loader import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client['news_bot']  
news_collection = db['news']  
