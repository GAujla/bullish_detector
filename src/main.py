"""Main file to query polymarket."""

# import webbrowser
# # webbrowser.open('https://polymarket.com/finance')

import re
import sys

import bs4
import requests  # type: ignore[import-untyped]

GAMMA_API_URL = "https://gamma-api.polymarket.com/events"
POLYMARKET_URL = "https://polymarket.com"


print("Searching...")
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(POLYMARKET_URL + "/" + " ".join(sys.argv[1:]), headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
web_page_data = soup.select("p")

matches = set(
    [p for p in web_page_data if re.search(r"finish", p.get_text(), re.IGNORECASE)]
)

first_match = list(matches)[0]
for p in matches:
    parent_link = p.parent.parent.parent.parent
    if parent_link and parent_link.name == "a":
        parent_link = parent_link.get("href")
        slug = parent_link.split("/")[-1]
    else:
        print("cant find link")

    api_res = requests.get(f"{GAMMA_API_URL}?slug={slug}", headers=headers)

    data = api_res.json()

    if data:
        event = data[0]
        title = event.get("title")
        print(f"Market: {title}")

        for market in event.get("markets", []):
            outcome_label = market.get("groupItemTitle", "Price")
            raw_price = market.get("outcomePrices", ["0"])[0]
            # Convert to dollar format
            price = raw_price
            print(f"  -> {outcome_label}")
