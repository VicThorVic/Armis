from abc import ABC, abstractmethod
from typing import List
import logging

from app.models.vendor_a import VendorAPost
from app.models.vendor_b import VendorBAlbum
from app.services.deduplicate import deduplicate_data
from app.services.fetch import fetch_data
from app.services.normalize import normalize_raw_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataProcessingStrategy(ABC):
    @abstractmethod
    async def fetch_all_data(self, page: int = 1, limit: int = 10):
        pass

    @abstractmethod
    def normalize_data(self, raw_data: list) -> list:
        pass

    @abstractmethod
    def deduplicate(self, data: list) -> list:
        pass


class VendorAStrategy(DataProcessingStrategy):
    @staticmethod
    async def fetch_all_data(page: int = 1, limit: int = 10):
        url = "https://jsonplaceholder.typicode.com/posts"
        return await fetch_data(url=url, page=page, limit=limit)

    @staticmethod
    def normalize_data(raw_data: List[dict]) -> List[VendorAPost]:
        return normalize_raw_data(raw_data=raw_data, model=VendorAPost)

    @staticmethod
    def deduplicate(data: List[VendorAPost]) -> List[VendorAPost]:
        return deduplicate_data(data)


class VendorBStrategy(DataProcessingStrategy):
    @staticmethod
    async def fetch_all_data(page: int = 1, limit: int = 10):
        url = "https://jsonplaceholder.typicode.com/albums"
        return await fetch_data(url=url, page=page, limit=limit)

    @staticmethod
    def normalize_data(raw_data: List[dict]) -> List[VendorBAlbum]:
        return normalize_raw_data(raw_data=raw_data, model=VendorBAlbum)

    @staticmethod
    def deduplicate(data: List[VendorBAlbum]) -> List[VendorBAlbum]:
        return deduplicate_data(data)


class DataProcessingStrategyFactory:
    @staticmethod
    def get_strategy(vendor_name: str) -> DataProcessingStrategy:
        """Factory method to return the appropriate strategy based on the vendor."""
        if vendor_name == "VendorA":
            return VendorAStrategy()
        elif vendor_name == "VendorB":
            return VendorBStrategy()
        else:
            raise ValueError(f"Unsupported vendor: {vendor_name}")
