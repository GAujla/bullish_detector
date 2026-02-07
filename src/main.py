"""Python Module to execute main block of code."""

from polymarket_scraper_wip import PolymarketExtract


def main() -> None:
    """Run main block of code."""
    pe = PolymarketExtract()
    pe.get_finance_market_information()


if __name__ == "__main__":
    main()
