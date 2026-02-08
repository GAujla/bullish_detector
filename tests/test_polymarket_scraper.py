# mypy: disable-error-code=no-untyped-def

from unittest.mock import patch

import pytest

from src.polymarket_scraper import PolymarketExtract
from tests.fixture_data.polymarket_scraper_fixture_data import finance_market_fixture_data


class TestPolymarketExtract:
    def test_polymarketextract_init_method(self):
        extractor = PolymarketExtract()
        assert extractor.gamma_api_base == "https://gamma-api.polymarket.com"
        assert isinstance(extractor.gamma_api_base, str)

    def test_polymarketextractor_init_custom_method(self):
        custom_url = "https://custom-url.hello.com"
        extractor = PolymarketExtract(custom_url)
        assert extractor.gamma_api_base == custom_url
        assert isinstance(extractor.gamma_api_base, str)

    @pytest.mark.parametrize("mock_api_response, expected_output", finance_market_fixture_data)
    @patch("requests.get")
    def test_get_finance_market_information(self, mock_get, mock_api_response, expected_output):
        extractor = PolymarketExtract()
        extractor.gamma_api_base = "https://api.gamma.example.com"

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_api_response

        results = extractor.get_finance_market_information()
        assert results == expected_output

        mock_get.assert_called_once_with(
            "https://api.gamma.example.com/public-search", params={"q": "closes week", "limit": 100}
        )
