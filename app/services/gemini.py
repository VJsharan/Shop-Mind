"""
ShopMind Gemini AI Service.

Two core functions:
1. parse_intent — extracts structured shopping filters from natural language
2. generate_explanations — produces per-product "why this" explanations

Both use Gemini 1.5 Flash via the vertexai SDK with in-memory caching.
"""

import asyncio
import json
import logging
from typing import Any

from vertexai.generative_models import GenerativeModel, GenerationConfig

from app.cache import get_cached, make_cache_key, set_cached
from app.models import ParsedIntent, Product, ProductResult

logger: logging.Logger = logging.getLogger("shopmind.gemini")

INTENT_SYSTEM_PROMPT: str = """You are a retail assistant intent parser. Given a user shopping query, extract structured filters.
Return ONLY valid JSON matching this schema:
{
  "category": string or null,
  "color": string or null,
  "max_price": number or null,
  "occasion": string or null,
  "keywords": [string]
}

Valid categories: shirts, trousers, shoes, tshirts, jackets, kurta, dresses, watches, bags, sunglasses, ethnic, shorts, trackpants, belts, wallets
Valid occasions: interview, office, casual, formal, gym, sports, college, wedding, festive, outing, party, travel

Do not include any explanation. Return only the JSON object."""

EXPLANATION_SYSTEM_PROMPT: str = """You are a helpful shopping assistant. Given a user query and a list of products, return a JSON array.
Each element must have:
{
  "product_id": string,
  "relevance_score": float between 0.0 and 1.0,
  "explanation": string
}
The explanation should be 1-2 sentences explaining why this product matches the user's query.
Sort by relevance_score descending. Return ONLY the JSON array."""


def _get_model() -> GenerativeModel:
    """Return a Gemini 1.5 Flash model instance."""
    return GenerativeModel("gemini-1.5-flash")


def _clean_json_response(text: str) -> str:
    """Strip markdown code fences and whitespace from Gemini response."""
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def _sync_call_gemini(system_prompt: str, user_prompt: str) -> str:
    """Synchronous Gemini API call. Wrapped in asyncio.to_thread by callers."""
    model: GenerativeModel = _get_model()
    config: GenerationConfig = GenerationConfig(
        temperature=0.1,
        max_output_tokens=2048,
    )
    response = model.generate_content(
        [system_prompt, user_prompt],
        generation_config=config,
    )
    return response.text


async def parse_intent(query: str) -> ParsedIntent:
    """Parse a natural language shopping query into structured filters."""
    cache_key: str = make_cache_key(f"intent:{query}")
    cached: Any | None = get_cached(cache_key)
    if cached is not None:
        logger.info("Cache hit for intent parsing (query_len=%d)", len(query))
        return cached

    try:
        raw_response: str = await asyncio.to_thread(
            _sync_call_gemini,
            INTENT_SYSTEM_PROMPT,
            f"User query: {query}",
        )
        cleaned: str = _clean_json_response(raw_response)
        parsed: dict[str, Any] = json.loads(cleaned)

        intent: ParsedIntent = ParsedIntent(
            category=parsed.get("category"),
            color=parsed.get("color"),
            max_price=parsed.get("max_price"),
            occasion=parsed.get("occasion"),
            keywords=parsed.get("keywords", []),
            raw_query=query,
        )
        set_cached(cache_key, intent)
        logger.info("Intent parsed: category=%s color=%s max_price=%s occasion=%s",
                     intent.category, intent.color, intent.max_price, intent.occasion)
        return intent

    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        logger.warning("Gemini intent parse failed: %s", type(exc).__name__)
        fallback: ParsedIntent = ParsedIntent(
            category=None,
            color=None,
            max_price=None,
            occasion=None,
            keywords=[],
            raw_query=query,
        )
        return fallback


async def generate_explanations(
    query: str, products: list[Product]
) -> list[ProductResult]:
    """Generate per-product relevance scores and explanations."""
    if not products:
        return []

    sorted_ids: str = ",".join(sorted(p.id for p in products))
    cache_key: str = make_cache_key(f"explain:{query}:{sorted_ids}")
    cached: Any | None = get_cached(cache_key)
    if cached is not None:
        logger.info("Cache hit for explanations (query_len=%d, products=%d)",
                     len(query), len(products))
        return cached

    product_summaries: list[dict[str, Any]] = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "color": p.color,
            "occasion": p.occasion,
            "description": p.description,
        }
        for p in products
    ]

    user_prompt: str = (
        f"User query: {query}\n\n"
        f"Products:\n{json.dumps(product_summaries, indent=2)}"
    )

    try:
        raw_response: str = await asyncio.to_thread(
            _sync_call_gemini,
            EXPLANATION_SYSTEM_PROMPT,
            user_prompt,
        )
        cleaned: str = _clean_json_response(raw_response)
        explanations: list[dict[str, Any]] = json.loads(cleaned)

        product_map: dict[str, Product] = {p.id: p for p in products}
        results: list[ProductResult] = []

        for item in explanations:
            pid: str = item.get("product_id", "")
            if pid in product_map:
                results.append(ProductResult(
                    product=product_map[pid],
                    relevance_score=min(1.0, max(0.0, float(item.get("relevance_score", 0.5)))),
                    explanation=item.get("explanation", "Matches your search criteria."),
                ))

        results.sort(key=lambda r: r.relevance_score, reverse=True)
        set_cached(cache_key, results)
        logger.info("Generated explanations for %d/%d products",
                     len(results), len(products))
        return results

    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        logger.warning("Gemini explanation generation failed: %s", type(exc).__name__)
        return [
            ProductResult(
                product=p,
                relevance_score=0.5,
                explanation="Matches your search criteria.",
            )
            for p in products
        ]
