"""
ShopMind Products Router.

GET /api/products       — list products with optional limit
GET /api/products/{id}  — get a single product by ID
"""

import logging

from fastapi import APIRouter, HTTPException, Query

from app.models import Product
from app.services.firestore import get_all_products, get_product_by_id

logger: logging.Logger = logging.getLogger("shopmind.products")

router: APIRouter = APIRouter(prefix="/api", tags=["products"])


@router.get("/products", response_model=list[Product])
async def list_products(
    limit: int = Query(default=20, ge=1, le=100, description="Max products to return"),
) -> list[Product]:
    """Return a list of products from the catalog."""
    products: list[Product] = await get_all_products(limit=limit)
    logger.info("Listed %d products (limit=%d)", len(products), limit)
    return products


@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str) -> Product:
    """Return a single product by its document ID."""
    product: Product | None = await get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail=f"Product '{product_id}' not found")
    return product
