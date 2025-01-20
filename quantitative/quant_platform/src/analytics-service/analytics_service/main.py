from fastapi import FastAPI
from api import pricing, risk, backtesting

app = FastAPI()

app.include_router(pricing.router, prefix="/api")
app.include_router(risk.router, prefix="/api")
app.include_router(backtesting.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)