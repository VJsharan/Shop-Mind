"""
ShopMind — FastAPI Application Entry Point.

Initializes Vertex AI on startup, mounts routers, configures CORS,
and serves the frontend static file.
"""

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import vertexai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.routers.chat import router as chat_router
from app.routers.products import router as products_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
)
logger: logging.Logger = logging.getLogger("shopmind.main")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Initialize Vertex AI SDK on startup."""
    vertexai.init(
        project=settings.GCP_PROJECT_ID,
        location=settings.VERTEX_LOCATION,
    )
    logger.info(
        "Vertex AI initialized: project=%s location=%s",
        settings.GCP_PROJECT_ID,
        settings.VERTEX_LOCATION,
    )
    yield
    logger.info("ShopMind shutting down")


app: FastAPI = FastAPI(
    title="ShopMind",
    description="AI-powered natural language shopping assistant",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(products_router)

app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint for monitoring and load balancers."""
    return {"status": "ok", "service": "shopmind"}


@app.get("/")
async def serve_frontend() -> FileResponse:
    """Serve the single-page frontend."""
    return FileResponse("frontend/index.html", media_type="text/html")
