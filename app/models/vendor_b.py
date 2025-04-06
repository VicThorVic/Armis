from pydantic import BaseModel


class VendorBAlbum(BaseModel):
    id: int
    userId: int
    title: str
