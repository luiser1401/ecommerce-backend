import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.data import init_db
from app.exceptions import EcommerceBackendException
from app.web import v1_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Lifespan event handler for the FastAPI application.
    This runs on startup and shutdown of the application.
    """
    try:
        # Startup logic
        logger.info("Application startup...")
        
        # Initialize database
        logger.info("Initializing database...")
        init_db()
        logger.info("Database initialized successfully")
        
        yield
        
        # Shutdown logic
        logger.info("Application shutdown...")
        logger.info("Closing database connections...")
    except Exception as e:
        logger.error(f"Failed to startup application: {e}")
        raise EcommerceBackendException(f"Application startup failed: {str(e)}")


app = FastAPI(title="ecommerce backend",
              lifespan=lifespan,
              servers=[
                  {"url": "http://localhost:8000"}
              ]
              )
app.include_router(v1_router)


@app.get("/health-check")
def health_check():
    return "OK"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
