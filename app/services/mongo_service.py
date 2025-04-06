import logging
from motor.motor_asyncio import AsyncIOMotorDatabase

logger = logging.getLogger(__name__)


async def save_to_mongo(data: list[dict], db: AsyncIOMotorDatabase) -> None:
    """
    Save the data to the MongoDB collection.

    :param data: List of data to save
    :param db: The MongoDB database session (injected by FastAPI dependency)
    """
    try:
        collection = db["test_collection"]  # Replace with your collection name
        # Insert many documents into the collection
        result = await collection.insert_many(data)
        # Log the number of inserted records
        logging.info(f"Inserted {len(result.inserted_ids)} records")
    except Exception as e:
        logging.error(f"Error saving data to MongoDB: {e}")
