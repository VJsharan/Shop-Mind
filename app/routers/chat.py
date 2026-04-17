"""
ShopMind Chat Router.

POST /api/chat — accepts a natural language query, returns ranked products
with AI-generated explanations.
"""

import logging

from fastapi import APIRouter, HTTPException

from app.models import ChatRequest, ChatResponse, ParsedIntent, ProductResult, Product
from app.services.gemini import parse_intent, generate_explanations
from app.services.firestore import query_products

logger: logging.Logger = logging.getLogger("shopmind.chat")

router: APIRouter = APIRouter(prefix="/api", tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Process a natural language shopping query and return ranked products."""
    logger.info(
        "Chat request: session=%s query_len=%d",
        request.session_id,
        len(request.query),
    )

    try:
        intent: ParsedIntent = await parse_intent(request.query)
    except Exception:
        logger.exception("Intent parsing failed")
        intent = ParsedIntent(raw_query=request.query)

    try:
        products: list[Product] = await query_products(intent)
    except Exception:
        logger.exception("Firestore query failed")
        raise HTTPException(status_code=503, detail="Product search temporarily unavailable")

    try:
        results: list[ProductResult] = await generate_explanations(
            request.query, products
        )
    except Exception:
        logger.exception("Explanation generation failed")
        results = [
            ProductResult(
                product=p,
                relevance_score=0.5,
                explanation="Matches your search criteria.",
            )
            for p in products
        ]

    if results:
        summary: str = (
            f"Found {len(results)} product{'s' if len(results) != 1 else ''} "
            f"matching your search. Here are the best picks ranked by relevance."
        )
    else:
        summary = (
            "No products found matching your criteria. "
            "Try broadening your search or using different keywords."
        )

    logger.info(
        "Chat response: session=%s results=%d",
        request.session_id,
        len(results),
    )

    return ChatResponse(
        results=results,
        summary=summary,
        parsed_intent=intent,
    )
