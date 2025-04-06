from pydantic import BaseModel


class VendorAPost(BaseModel):
    id: int
    title: str
    body: str
