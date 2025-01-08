from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class BacktestRequest(BaseModel):
    strategy_id: int
    historical_data: list

class BacktestResponse(BaseModel):
    strategy_id: int
    performance: float

@router.get("/backtest/{strategy_id}", response_model=BacktestResponse)
async def get_backtest(strategy_id: int):
    performance = 0.05  # Example logic
    return BacktestResponse(strategy_id=strategy_id, performance=performance)

@router.post("/backtest", response_model=BacktestResponse)
async def run_backtest(backtest_request: BacktestRequest):
    performance = 0.05  # Example logic
    return BacktestResponse(strategy_id=backtest_request.strategy_id, performance=performance)