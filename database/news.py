from .db import news_collection

async def get_news_by_category(category: str):
    cursor = news_collection.find({"category": category}).sort("created_at", -1)
    return [news async for news in cursor]
