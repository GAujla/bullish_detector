"""Python module to handle extracting information from polymrket."""

import json
from collections import defaultdict
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
                    "title": information.get("title"),  # Just to showcase we can get this, not utilised
                    "information": "Closed" if information.get("closed") else "Open",
                    "slug": information.get("slug"),
                    "volume": information.get("volume"),  # Just to showcase we can get this, not utilised
                    "end_date": information.get("endDate"),  # Just to showcase we can get this, not utilised
                }
            )
        return results

    def get_financial_values(self) -> defaultdict[str, List] | None:
        """Utilises slug value (key indicatior to identify stocks when using event api).

        This is done to extract key information relevant to a particular bet for a specific stock.
        """
        betting_ticket_result = self.get_finance_market_information()

        market_and_price_output = defaultdict(list)

        for bet in betting_ticket_result:
            slug = bet["slug"]
            response = requests.get(f"{self.gamma_api_base}/events?slug={slug}")
            data = response.json()

            if not data:
                continue
            event = data[0]
            title = event.get("title")

            for market in event.get("markets", []):
                outcome_label = market.get("groupItemTitle")
                market_and_price_output[title].append(outcome_label)
                market_and_price_output[title].append(market.get("outcomePrices"))

        return market_and_price_output

    def get_comments_for_polymarket_event(self) -> None:
        """Perform retrieval of comments from Polymarket betting for each page.

        This function gets the username and comment relating to each
        polymarket bet from the get_finance_market_information
        function.
        """
        # TODO we seem to repeat ourselves lets write this in a function
        endpoint = f"{self.gamma_api_base}/comments"
        betting_ticket_result = self.get_finance_market_information()

        for bet in betting_ticket_result:
            slug = bet["slug"]
            response = requests.get(f"{self.gamma_api_base}/events?slug={slug}")
            print(slug)
            data = response.json()
            first = data[0]
            parent_entity_id = first["series"][0]["id"]
            params = {"parent_entity_id": parent_entity_id, "parent_entity_type": "Series"}

            response_com = requests.get(endpoint, params)
            comment_information = response_com.json()

            json_str = json.dumps(comment_information, indent=4)
            with open("sample.json", "a") as f:
                f.write(json_str)
            for comment in comment_information:
                messgae = comment["body"]
                name = comment["profile"]["name"]
                print(f"{name}: {messgae}")


if __name__ == "__main__":
    p = PolymarketExtract()
    p.get_comments_for_polymarket_event()
