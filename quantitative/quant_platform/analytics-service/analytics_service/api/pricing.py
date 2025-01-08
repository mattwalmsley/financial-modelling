from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PriceRequest(BaseModel):
    item_id: int
    quantity: int

class PriceResponse(BaseModel):
    item_id: int
    total_price: float

@router.get("/price/{item_id}", response_model=PriceResponse)
async def get_price(item_id: int, quantity: int):
    price_per_item = 10.0  # Example logic
    total_price = price_per_item * quantity
    return PriceResponse(item_id=item_id, total_price=total_price)

@router.post("/price", response_model=PriceResponse)
async def calculate_price(price_request: PriceRequest):
    price_per_item = 10.0  # Example logic
    total_price = price_per_item * price_request.quantity
    return PriceResponse(item_id=price_request.item_id, total_price=total_price)