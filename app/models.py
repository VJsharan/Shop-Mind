"""
ShopMind Pydantic v2 Models.

All request/response schemas for the API. Strict types, no Optional without defaults.
"""

from pydantic import BaseModel, Field


class Product(BaseModel):
    """A single product from the Firestore catalog."""

    id: str
    name: str
    category: str
    sub_category: str
    color: str
    price: float
    brand: str
    occasion: list[str]
    sizes: list[str]
    rating: float
    stock: int
    description: str


class ParsedIntent(BaseModel):
    """Structured filters extracted from a natural language query by Gemini."""

    category: str | None = None
    color: str | None = None
    max_price: float | None = None
    occasion: str | None = None
    keywords: list[str] = Field(default_factory=list)
    raw_query: str = ""


class ProductResult(BaseModel):
    """A product matched to a query with relevance score and AI explanation."""

    product: Product
    relevance_score: float = Field(ge=0.0, le=1.0)
    explanation: str


class ChatRequest(BaseModel):
    """Incoming chat request from the frontend."""

    query: str = Field(min_length=1, max_length=500)
    session_id: str = Field(min_length=1)


class ChatResponse(BaseModel):
    """Full response returned to the frontend after processing a chat query."""

    results: list[ProductResult]
    summary: str
    parsed_intent: ParsedIntent
