from typing import Type
from pydantic import BaseModel


def deduplicate_data(data: list[Type[BaseModel]]) -> list[Type[BaseModel]]:
    seen = set()
    deduplicated = []
    for post in data:
        if post.title not in seen:
            seen.add(post.title)
            deduplicated.append(post)
    return deduplicated
