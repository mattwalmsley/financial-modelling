import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from requests import Request

from api import pricing, risk, backtesting
from logger import Logger

logger = Logger()


@asynccontextmanager
async def lifespan(application: FastAPI):
    # Startup logic
    logger.info("Starting up the application...")
    yield
    # Shutdown logic
    logger.info("Shutting down the application...")


app = FastAPI(lifespan=lifespan)

app.include_router(pricing.router, prefix="/api")
app.include_router(risk.router, prefix="/api")
app.include_router(backtesting.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.addHandler(logger.file_handler)  # Reuse the same file handler

    uvicorn_error_logger = logging.getLogger("uvicorn.error")
    uvicorn_error_logger.addHandler(logger.file_handler)

    uvicorn_access_logger = logging.getLogger("uvicorn.access")
    uvicorn_access_logger.addHandler(logger.file_handler)

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config=None,  # Disable Uvicorn's default logging config
        log_level="info",  # Set the log level
    )
