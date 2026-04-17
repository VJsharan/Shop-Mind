"""
ShopMind Firestore Service.

Async-compatible Firestore client for querying the product catalog.
Uses the synchronous Firestore client wrapped in asyncio.to_thread
for non-blocking operation within the async FastAPI stack.
"""

import asyncio
import logging
from typing import Any

from google.cloud import firestore

from app.config import settings
from app.models import ParsedIntent, Product

logger: logging.Logger = logging.getLogger("shopmind.firestore")

_db: firestore.Client | None = None


def _get_db() -> firestore.Client:
    """Lazy-initialize and return the Firestore client singleton."""
    global _db
    if _db is None:
        _db = firestore.Client(
            project=settings.GCP_PROJECT_ID,
            database=settings.FIRESTORE_DATABASE,
        )
        logger.info("Firestore client initialized for project=%s db=%s",
                     settings.GCP_PROJECT_ID, settings.FIRESTORE_DATABASE)
    return _db


def _sync_query_products(intent: ParsedIntent) -> list[dict[str, Any]]:
    """Synchronous Firestore query with progressive filter application."""
    db = _get_db()
    query: Any = db.collection("products")

    has_filters: bool = False

    if intent.category:
        query = query.where(filter=firestore.FieldFilter("category", "==", intent.category))
        has_filters = True

    if intent.color:
        query = query.where(filter=firestore.FieldFilter("color", "==", intent.color))
        has_filters = True

    if intent.max_price is not None:
        query = query.where(filter=firestore.FieldFilter("price", "<=", intent.max_price))
        has_filters = True

    docs = list(query.limit(20).stream())

    if not docs and has_filters:
        logger.info("No results with filters, falling back to full scan")
        docs = list(db.collection("products").limit(20).stream())

    return [doc.to_dict() for doc in docs]


def _sync_get_all_products(limit: int) -> list[dict[str, Any]]:
    """Synchronous fetch of all products up to limit."""
    db = _get_db()
    docs = list(db.collection("products").limit(limit).stream())
    return [doc.to_dict() for doc in docs]


def _sync_get_product_by_id(product_id: str) -> dict[str, Any] | None:
    """Synchronous fetch of a single product by document ID."""
    db = _get_db()
    doc = db.collection("products").document(product_id).get()
    if doc.exists:
        return doc.to_dict()
    return None


async def query_products(intent: ParsedIntent) -> list[Product]:
    """Query Firestore products based on parsed intent filters (async)."""
    raw_results: list[dict[str, Any]] = await asyncio.to_thread(
        _sync_query_products, intent
    )
    products: list[Product] = []
    for data in raw_results:
        try:
            products.append(Product(**data))
        except Exception:
            logger.warning("Skipping malformed product document id=%s",
                           data.get("id", "unknown"))
    logger.info("query_products returned %d results", len(products))
    return products


async def get_all_products(limit: int = 20) -> list[Product]:
    """Fetch all products up to the given limit (async)."""
    raw_results: list[dict[str, Any]] = await asyncio.to_thread(
        _sync_get_all_products, limit
    )
    products: list[Product] = []
    for data in raw_results:
        try:
            products.append(Product(**data))
        except Exception:
            logger.warning("Skipping malformed product document id=%s",
                           data.get("id", "unknown"))
    return products


async def get_product_by_id(product_id: str) -> Product | None:
    """Fetch a single product by its document ID (async)."""
    data: dict[str, Any] | None = await asyncio.to_thread(
        _sync_get_product_by_id, product_id
    )
    if data is None:
        return None
    try:
        return Product(**data)
    except Exception:
        logger.warning("Malformed product document id=%s", product_id)
        return None
