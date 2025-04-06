from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.settings import settings
import logging

logger = logging.getLogger(__name__)

# Global MongoDB client and database instance
mongo_client = None
database = None


async def startup_db():
    global mongo_client, database
    mongo_client = AsyncIOMotorClient(settings.MONGODB_URL)
    database = mongo_client[settings.MONGODB_DB]
    logger.info("MongoDB connection established")


async def shutdown_db():
    global mongo_client
    mongo_client.close()
    logger.info("MongoDB connection closed")


# Dependency for MongoDB session
def get_mongo_db() -> AsyncIOMotorDatabase:
    return database
