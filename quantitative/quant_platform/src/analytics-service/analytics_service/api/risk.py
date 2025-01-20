from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RiskRequest(BaseModel):
    asset_id: int
    exposure: float

class RiskResponse(BaseModel):
    asset_id: int
    risk_score: float

@router.get("/risk/{asset_id}", response_model=RiskResponse)
async def get_risk(asset_id: int, exposure: float):
    risk_score = exposure * 0.1  # Example logic
    return RiskResponse(asset_id=asset_id, risk_score=risk_score)

@router.post("/risk", response_model=RiskResponse)
async def calculate_risk(risk_request: RiskRequest):
    risk_score = risk_request.exposure * 0.1  # Example logic
    return RiskResponse(asset_id=risk_request.asset_id, risk_score=risk_score)