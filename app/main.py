import logging
from typing import Literal
from app.core.mongo_db import get_mongo_db, shutdown_db, startup_db
from fastapi import FastAPI, HTTPException, Depends, Request
from app.data_procesing_startegy import DataProcessingStrategyFactory
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi.responses import JSONResponse

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.services.mongo_service import save_to_mongo

# Set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_event_handler("startup", startup_db)
app.add_event_handler("shutdown", shutdown_db)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
async def ratelimit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(content={"detail": "Rate limit exceeded"}, status_code=429)


@app.get("/fetch-data")
@limiter.limit("5/minute")  # Only 5 requests per minute
async def fetch_data(
    request: Request,
    vendor_name: Literal["VendorA", "VendorB"],
    batch_size: int = 50,
    db: AsyncIOMotorDatabase = Depends(get_mongo_db),
):
    try:
        # Step 1: Get the vendor-specific data processing strategy
        strategy = DataProcessingStrategyFactory.get_strategy(vendor_name)
        page = 1

        while True:
            # Fetch Data (raw dictionary from the API)
            data = await strategy.fetch_all_data(page=page, limit=batch_size)
            if not data:
                break  # Exit the loop if no more data is returned

            # Step 3: Normalize the data using vendor-specific strategy
            normalized_data = strategy.normalize_data(data)
            # Step 4: Deduplicate the normalized data using the vendor's strategy
            deduped_data = strategy.deduplicate(normalized_data)

            # Step 5: Save to MongoDB (convert Pydantic models to dicts)
            dict_data = [post.dict() for post in deduped_data]
            await save_to_mongo(dict_data, db)  # Pass db as the dependency

            page += 1

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
