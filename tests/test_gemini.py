"""
Tests for the Gemini intent parser service.

Uses unittest.mock to avoid hitting live Gemini APIs.
"""

import json
from unittest.mock import patch, MagicMock

import pytest

from app.cache import clear_cache
from app.models import ParsedIntent


@pytest.fixture(autouse=True)
def _clear_cache_before_each() -> None:
    """Ensure cache is clean before every test."""
    clear_cache()


class TestParseIntentFormalShirt:
    """Test that parse_intent correctly extracts filters for a formal shirt query."""

    @pytest.mark.asyncio
    async def test_parse_intent_formal_shirt(self) -> None:
        mock_response: dict[str, object] = {
            "category": "shirts",
            "color": "blue",
            "max_price": 1500,
            "occasion": "interview",
            "keywords": ["formal", "shirt", "blue"],
        }

        mock_model_instance: MagicMock = MagicMock()
        mock_result: MagicMock = MagicMock()
        mock_result.text = json.dumps(mock_response)
        mock_model_instance.generate_content.return_value = mock_result

        with patch(
            "app.services.gemini._get_model", return_value=mock_model_instance
        ):
            from app.services.gemini import parse_intent

            intent: ParsedIntent = await parse_intent(
                "blue formal shirt under 1500 for an interview"
            )

        assert intent.category == "shirts"
        assert intent.color == "blue"
        assert intent.max_price == 1500
        assert intent.occasion == "interview"
        assert len(intent.keywords) >= 1


class TestParseIntentFallback:
    """Test that parse_intent returns a safe fallback on malformed Gemini output."""

    @pytest.mark.asyncio
    async def test_parse_intent_fallback_on_bad_json(self) -> None:
        mock_model_instance: MagicMock = MagicMock()
        mock_result: MagicMock = MagicMock()
        mock_result.text = "this is not valid json at all {{{}"
        mock_model_instance.generate_content.return_value = mock_result

        with patch(
            "app.services.gemini._get_model", return_value=mock_model_instance
        ):
            from app.services.gemini import parse_intent

            intent: ParsedIntent = await parse_intent("some random query")

        assert intent.category is None
        assert intent.color is None
        assert intent.max_price is None
        assert intent.occasion is None
        assert intent.raw_query == "some random query"


class TestCacheHitSkipsGemini:
    """Test that calling parse_intent twice with the same query only calls Gemini once."""

    @pytest.mark.asyncio
    async def test_cache_hit_skips_gemini(self) -> None:
        mock_response: dict[str, object] = {
            "category": "shoes",
            "color": "black",
            "max_price": 3000,
            "occasion": "formal",
            "keywords": ["formal", "shoes"],
        }

        mock_model_instance: MagicMock = MagicMock()
        mock_result: MagicMock = MagicMock()
        mock_result.text = json.dumps(mock_response)
        mock_model_instance.generate_content.return_value = mock_result

        with patch(
            "app.services.gemini._get_model", return_value=mock_model_instance
        ):
            from app.services.gemini import parse_intent

            query: str = "black formal shoes under 3000"

            intent_1: ParsedIntent = await parse_intent(query)
            intent_2: ParsedIntent = await parse_intent(query)

        assert intent_1.category == "shoes"
        assert intent_2.category == "shoes"
        assert mock_model_instance.generate_content.call_count == 1
