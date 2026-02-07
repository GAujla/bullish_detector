"""Python module to handle extracting information from polymrket."""

from typing import List

import requests


class PolymarketExtract:
    """PolymarketExtract class revolved around extracting informationfrom polymarket."""

    def __init__(self, gamma_api_base: str = "https://gamma-api.polymarket.com") -> None:
        """Init constructor method.

        Args:
        ----
            gamma_api_base (str, optional): Polymarket Api. Defaults to "https://gamma-api.polymarket.com".
        """
        self.gamma_api_base = gamma_api_base

    def get_finance_market_information(self) -> List[dict]:
        """Perform extraction of financial bets related to query.

        Getting a public search of open bets regarding a specific parameter query.
        Extracts title, information, slug, volume and enddate which is stored in a csv file.
        """
        results = []
        endpoint = f"{self.gamma_api_base}/public-search"
        # params = {"q": "closes week", "active": "true"}
        params = {"q": "closes week", "limit": 100}
        response = requests.get(endpoint, params=params)
        data = response.json()
        data_list = data.get("events", [])

        for information in data_list:
            results.append(
                {
                    "title": information.get("title"),
                    "information": "Closed" if information.get("closed") else "Open",
                    "slug": information.get("slug"),
                    "volume": information.get("volume"),
                    "end_date": information.get("endDate"),
                }
            )
        return results

    def get_price_value(self) -> None:
        """Utilises slug value (key indicatior to identify stocks when using event api).

        This is done to extract key information relevant to a particular bet for a specific stock.
        """
        betting_ticket_result = self.get_finance_market_information()
        for bet in betting_ticket_result:
            # if bet['information'] == 'Closed':
            slug = bet["slug"]
            response = requests.get(f"{self.gamma_api_base}/events?slug={slug}")
            data = response.json()

            event = data[0]
            title = event.get("title")
            print(f"Market: {title}")

            for market in event.get("markets", []):
                outcome_label = market.get("groupItemTitle", "Price")
                print(f"  {outcome_label}")
