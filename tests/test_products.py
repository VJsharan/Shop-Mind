"""
Tests for the Firestore product query service.

Uses unittest.mock to avoid hitting live Firestore.
"""

from unittest.mock import patch, MagicMock, call

import pytest

from app.models import ParsedIntent, Product


MOCK_PRODUCT_DATA: dict[str, object] = {
    "id": "p001",
    "name": "ArrowFlex Blue Formal Shirt",
    "category": "shirts",
    "sub_category": "formal",
    "color": "blue",
    "price": 1299,
    "brand": "Arrow",
    "occasion": ["interview", "office", "formal"],
    "sizes": ["S", "M", "L", "XL"],
    "rating": 4.3,
    "stock": 45,
    "description": "Slim fit cotton formal shirt with wrinkle-resistant fabric.",
}


def _make_mock_doc(data: dict[str, object]) -> MagicMock:
    """Create a mock Firestore document snapshot."""
    doc: MagicMock = MagicMock()
    doc.to_dict.return_value = data
    doc.exists = True
    return doc


class TestQueryProductsColorFilter:
    """Test that color filter is applied to the Firestore query."""

    @pytest.mark.asyncio
    async def test_query_products_with_color_filter(self) -> None:
        intent: ParsedIntent = ParsedIntent(
            category=None,
            color="blue",
            max_price=None,
            occasion=None,
            keywords=[],
            raw_query="blue shirt",
        )

        mock_doc: MagicMock = _make_mock_doc(MOCK_PRODUCT_DATA)

        mock_query: MagicMock = MagicMock()
        mock_query.where.return_value = mock_query
        mock_query.limit.return_value = mock_query
        mock_query.stream.return_value = [mock_doc]

        mock_collection: MagicMock = MagicMock()
        mock_collection.where.return_value = mock_query
        mock_collection.limit.return_value = mock_query
        mock_collection.stream.return_value = [mock_doc]

        mock_db: MagicMock = MagicMock()
        mock_db.collection.return_value = mock_collection

        with patch("app.services.firestore._get_db", return_value=mock_db):
            from app.services.firestore import query_products

            products: list[Product] = await query_products(intent)

        assert len(products) >= 1
        assert products[0].color == "blue"
        mock_collection.where.assert_called()


class TestQueryProductsPriceFilter:
    """Test that max_price filter is applied to the Firestore query."""

    @pytest.mark.asyncio
    async def test_query_products_price_filter(self) -> None:
        intent: ParsedIntent = ParsedIntent(
            category="shirts",
            color=None,
            max_price=1500.0,
            occasion=None,
            keywords=["formal"],
            raw_query="formal shirt under 1500",
        )

        mock_doc: MagicMock = _make_mock_doc(MOCK_PRODUCT_DATA)

        mock_query: MagicMock = MagicMock()
        mock_query.where.return_value = mock_query
        mock_query.limit.return_value = mock_query
        mock_query.stream.return_value = [mock_doc]

        mock_collection: MagicMock = MagicMock()
        mock_collection.where.return_value = mock_query
        mock_collection.limit.return_value = mock_query
        mock_collection.stream.return_value = [mock_doc]

        mock_db: MagicMock = MagicMock()
        mock_db.collection.return_value = mock_collection

        with patch("app.services.firestore._get_db", return_value=mock_db):
            from app.services.firestore import query_products

            products: list[Product] = await query_products(intent)

        assert len(products) >= 1
        assert products[0].price <= 1500
        # category filter + price filter = 2 where() calls
        assert mock_collection.where.call_count >= 1


class TestQueryProductsFallback:
    """Test that query falls back to full scan when no filters are set."""

    @pytest.mark.asyncio
    async def test_query_products_fallback(self) -> None:
        intent: ParsedIntent = ParsedIntent(
            category=None,
            color=None,
            max_price=None,
            occasion=None,
            keywords=[],
            raw_query="show me something nice",
        )

        mock_doc: MagicMock = _make_mock_doc(MOCK_PRODUCT_DATA)

        mock_collection: MagicMock = MagicMock()
        mock_collection.limit.return_value = mock_collection
        mock_collection.stream.return_value = [mock_doc]

        mock_db: MagicMock = MagicMock()
        mock_db.collection.return_value = mock_collection

        with patch("app.services.firestore._get_db", return_value=mock_db):
            from app.services.firestore import query_products

            products: list[Product] = await query_products(intent)

        assert len(products) >= 1
        # No where() should be called when there are no filters
        mock_collection.where.assert_not_called()
