"""Python module for Polymarket scraping."""
import re
import sys

import bs4
import requests
from bs4.element import Tag


def query_web_page(
    polymarket_url: str = "https://polymarket.com",
    headers: dict[str, str] = {"User-Agent": "Mozilla/5.0"},  # noqa B006
) -> list[Tag]:
    """Query web page.

    Args:
    ----
        polymarket_url (str, optional): Polymarket URL. Defaults to "https://polymarket.com".
        headers (str, optional): Header useful for scripting to avoid being blocked.
        Defaults to {"User-Agent": "Mozilla/5.0"}.

    Returns:
    -------
        list[bs4.element.Tag]: Web page data returned from polymarket.
    """
    res = requests.get(polymarket_url + "/" + " ".join(sys.argv[1:]), headers=headers)
    print(sys.argv[1:])
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    web_page_data = soup.select("p")
    return list(web_page_data)


def get_price_value(
    web_page_data: list[Tag],
    headers: dict[str, str] = {"User-Agent": "Mozilla/5.0"},  # noqa B006
    gamma_api_url: str = "https://gamma-api.polymarket.com/events",
) -> None:
    """Extract price set for bets to be placed on.

    Args:
    ----
        web_page_data (bs4.element.Tag): Web page data.
        headers (str, optional): Header to avoid being blocked from scripting.
        Defaults to {"User-Agent": "Mozilla/5.0"}.
        gamma_api_url (str, optional): Polymarket API URL. Defaults to "https://gamma-api.polymarket.com/events".
    """
    matches = set([p for p in web_page_data if re.search(r"Gold", p.get_text(), re.IGNORECASE)])

    for p in matches:
        parent_link = p.parent.parent.parent.parent
        if parent_link and parent_link.name == "a":
            parent_link = parent_link.get("href")
            slug = parent_link.split("/")[-1]
        else:
            print("cant find link")
    print("this is ", slug)
    api_res = requests.get(f"{gamma_api_url}?slug={slug}", headers=headers)

    data = api_res.json()

    if data:
        event = data[0]
        title = event.get("title")
        print(f"Market: {title}")

        for market in event.get("markets", []):
            outcome_label = market.get("groupItemTitle", "Price")
            print(f"  {outcome_label}")
