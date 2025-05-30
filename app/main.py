"""Main application module."""

import contextlib
import uvicorn
from fastapi import FastAPI
from typing import AsyncGenerator

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Lifespan event handler for the FastAPI application.
    This runs on startup and shutdown of the application.
    """
    # Startup logic
    print("Application startup...")
    yield
    # Shutdown logic
    print("Application shutdown...")

app = FastAPI(title="Clean Architecture API", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Welcome to Clean Architecture API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
