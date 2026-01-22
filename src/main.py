"""Python Module to execute main block of code."""

from polymarket_scraper import get_price_value, query_web_page


def main() -> None:
    """Run main block of code."""
    web_page_data = query_web_page()
    get_price_value(web_page_data)


if __name__ == "__main__":
    main()
