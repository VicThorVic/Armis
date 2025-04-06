import logging
from typing import Type
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def normalize_raw_data(
    raw_data: list[dict], model: Type[BaseModel]
) -> list[Type[BaseModel]]:
    normalized_data = []
    for post in raw_data:
        try:
            normalized_data.append(model(**post))
        except Exception as e:
            logger.error(f"Error normalizing post: {post}. Error: {e}")
            continue  # Skip the problematic post
    return normalized_data
