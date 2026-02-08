"""Python Module to execute main block of code."""

from scraping_data.polymarket_scraper import PolymarketExtract


def main() -> None:
    """Run main block of code."""
    pe = PolymarketExtract()
    a = pe.get_price_value()
    print(a)


if __name__ == "__main__":
    main()
