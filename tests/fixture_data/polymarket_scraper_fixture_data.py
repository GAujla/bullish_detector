finance_market_fixture_data = [
    (
        {
            "events": [
                {
                    "title": "Will BTC close above 50k?",
                    "closed": False,
                    "slug": "btc-50k-close",
                    "volume": 1000.50,
                    "endDate": "2023-12-31",
                },
                {
                    "title": "ETH volume high?",
                    "closed": True,
                    "slug": "eth-vol",
                    "volume": 500,
                    "endDate": "2023-11-30",
                },
            ]
        },
        [
            {
                "title": "Will BTC close above 50k?",
                "information": "Open",
                "slug": "btc-50k-close",
                "volume": 1000.50,
                "end_date": "2023-12-31",
            },
            {
                "title": "ETH volume high?",
                "information": "Closed",
                "slug": "eth-vol",
                "volume": 500,
                "end_date": "2023-11-30",
            },
        ],
    ),
    ({"events": []}, []),
]


financial_values = [
    (
        [
            {
                "title": "Apple (AAPL) closes week of Feb 9 at ___?",
                "markets": [
                    {"groupItemTitle": "<$255", "outcomePrices": ["0.1845", "0.8155"]},
                    {"groupItemTitle": "$255-$260", "outcomePrices": ["0.4385", "0.5615"]},
                ],
            }
        ],
        {
            "Apple (AAPL) closes week of Feb 9 at ___?": [
                "<$255",
                ["0.1845", "0.8155"],
                "$255-$260",
                ["0.4385", "0.5615"],
            ]
        },
    ),
    ([], {}),
]
