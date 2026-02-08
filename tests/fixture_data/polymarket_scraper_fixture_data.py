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
