import httpx


async def fetch_data(url: str, page: int = 1, limit: int = 10) -> dict:
    params = {"_page": page, "_limit": limit}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        if response.status_code == 200:
            data = response.json()  # Parse JSON data
            return data
        else:
            return {"error": "Failed to fetch data"}
