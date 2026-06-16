regular_season_standings = [
    {
        "rank": 1,
        "team": "Aurora Gaming PH",
        "match": "13-1",
        "game": "26-10",
        "diff": 16,
        "pts": 13
    },
    {
        "rank": 2,
        "team": "ONIC Philippines",
        "match": "9-5",
        "game": "22-13",
        "diff": 9,
        "pts": 9
    },
    {
        "rank": 3,
        "team": "Team Liquid PH",
        "match": "9-5",
        "game": "21-12",
        "diff": 9,
        "pts": 9
    },
    {
        "rank": 4,
        "team": "Twisted Minds PH",
        "match": "6-8",
        "game": "16-20",
        "diff": -4,
        "pts": 6
    },
    {
        "rank": 5,
        "team": "TNC Pro Team",
        "match": "5-9",
        "game": "16-21",
        "diff": -5,
        "pts": 5
    },
    {
        "rank": 6,
        "team": "Team Falcons PH",
        "match": "5-9",
        "game": "15-21",
        "diff": -6,
        "pts": 5
    },
    {
        "rank": 7,
        "team": "Omega Esports",
        "match": "5-9",
        "game": "14-21",
        "diff": -7,
        "pts": 5
    },
    {
        "rank": 8,
        "team": "AP.Bren",
        "match": "4-10",
        "game": "11-23",
        "diff": -12,
        "pts": 4
    }
]

head_to_head_data = {
    1: [  # Aurora Gaming PH
        {"opponent_rank": 2, "score": [4, 2], "series": [[2, 1], [2, 1]]},  # vs ONIC Philippines
        {"opponent_rank": 3, "score": [4, 1], "series": [[2, 0], [2, 1]]},  # vs Team Liquid PH
        {"opponent_rank": 4, "score": [4, 1], "series": [[2, 1], [2, 0]]},  # vs Twisted Minds PH
        {"opponent_rank": 5, "score": [4, 1], "series": [[2, 1], [2, 0]]},  # vs TNC Pro Team
        {"opponent_rank": 6, "score": [4, 1], "series": [[2, 0], [2, 1]]},  # vs Team Falcons PH
        {"opponent_rank": 7, "score": [4, 1], "series": [[2, 0], [2, 1]]},  # vs Omega Esports
        {"opponent_rank": 8, "score": [4, 1], "series": [[2, 1], [2, 0]]}   # vs AP.Bren
    ],
    2: [  # ONIC Philippines
        {"opponent_rank": 1, "score": [2, 4], "series": [[1, 2], [1, 2]]},  # vs Aurora Gaming PH
        {"opponent_rank": 3, "score": [4, 0], "series": [[2, 0], [2, 0]]},  # vs Team Liquid PH
        {"opponent_rank": 4, "score": [3, 2], "series": [[1, 2], [2, 0]]},  # vs Twisted Minds PH
        {"opponent_rank": 5, "score": [4, 2], "series": [[2, 1], [2, 1]]},  # vs TNC Pro Team
        {"opponent_rank": 6, "score": [3, 2], "series": [[2, 0], [1, 2]]},  # vs Team Falcons PH
        {"opponent_rank": 7, "score": [4, 0], "series": [[2, 0], [2, 0]]},  # vs Omega Esports
        {"opponent_rank": 8, "score": [2, 2], "series": [[0, 2], [2, 0]]}   # vs AP.Bren
    ],
    3: [  # Team Liquid PH
        {"opponent_rank": 1, "score": [1, 4], "series": [[1, 2], [0, 2]]},  # vs Aurora Gaming PH
        {"opponent_rank": 2, "score": [0, 4], "series": [[0, 2], [0, 2]]},  # vs ONIC Philippines
        {"opponent_rank": 4, "score": [4, 1], "series": [[2, 0], [2, 1]]},  # vs Twisted Minds PH
        {"opponent_rank": 5, "score": [4, 0], "series": [[2, 0], [2, 0]]},  # vs TNC Pro Team
        {"opponent_rank": 6, "score": [3, 3], "series": [[2, 1], [1, 2]]},  # vs Team Falcons PH
        {"opponent_rank": 7, "score": [4, 0], "series": [[2, 0], [2, 0]]},  # vs Omega Esports
        {"opponent_rank": 8, "score": [4, 0], "series": [[2, 0], [2, 0]]}   # vs AP.Bren
    ],
    4: [  # Twisted Minds PH
        {"opponent_rank": 1, "score": [1, 4], "series": [[1, 2], [0, 2]]},  # vs Aurora Gaming PH
        {"opponent_rank": 2, "score": [2, 3], "series": [[2, 1], [0, 2]]},  # vs ONIC Philippines
        {"opponent_rank": 3, "score": [1, 4], "series": [[0, 2], [1, 2]]},  # vs Team Liquid PH
        {"opponent_rank": 5, "score": [3, 3], "series": [[2, 1], [1, 2]]},  # vs TNC Pro Team
        {"opponent_rank": 6, "score": [3, 2], "series": [[1, 2], [2, 0]]},  # vs Team Falcons PH
        {"opponent_rank": 7, "score": [2, 3], "series": [[0, 2], [2, 1]]},  # vs Omega Esports
        {"opponent_rank": 8, "score": [4, 1], "series": [[2, 0], [2, 1]]}   # vs AP.Bren
    ],
    5: [  # TNC Pro Team
        {"opponent_rank": 1, "score": [1, 4], "series": [[1, 2], [0, 2]]},  # vs Aurora Gaming PH
        {"opponent_rank": 2, "score": [2, 4], "series": [[1, 2], [1, 2]]},  # vs ONIC Philippines
        {"opponent_rank": 3, "score": [0, 4], "series": [[0, 2], [0, 2]]},  # vs Team Liquid PH
        {"opponent_rank": 4, "score": [3, 3], "series": [[1, 2], [2, 1]]},  # vs Twisted Minds PH
        {"opponent_rank": 6, "score": [4, 1], "series": [[2, 0], [2, 1]]},  # vs Team Falcons PH
        {"opponent_rank": 7, "score": [3, 3], "series": [[2, 1], [1, 2]]},  # vs Omega Esports
        {"opponent_rank": 8, "score": [4, 1], "series": [[2, 1], [2, 0]]}   # vs AP.Bren
    ],
    6: [  # Team Falcons PH
        {"opponent_rank": 1, "score": [1, 4], "series": [[0, 2], [1, 2]]},  # vs Aurora Gaming PH
        {"opponent_rank": 2, "score": [2, 3], "series": [[0, 2], [2, 1]]},  # vs ONIC Philippines
        {"opponent_rank": 3, "score": [3, 3], "series": [[1, 2], [2, 1]]},  # vs Team Liquid PH
        {"opponent_rank": 4, "score": [2, 3], "series": [[2, 1], [0, 2]]},  # vs Twisted Minds PH
        {"opponent_rank": 5, "score": [1, 4], "series": [[0, 2], [1, 2]]},  # vs TNC Pro Team
        {"opponent_rank": 7, "score": [2, 3], "series": [[2, 1], [0, 2]]},  # vs Omega Esports
        {"opponent_rank": 8, "score": [3, 2], "series": [[2, 0], [1, 2]]}   # vs AP.Bren
    ],
    7: [  # Omega Esports
        {"opponent_rank": 1, "score": [1, 4], "series": [[0, 2], [1, 2]]},  # vs Aurora Gaming PH
        {"opponent_rank": 2, "score": [0, 4], "series": [[0, 2], [0, 2]]},  # vs ONIC Philippines
        {"opponent_rank": 3, "score": [0, 4], "series": [[0, 2], [0, 2]]},  # vs Team Liquid PH
        {"opponent_rank": 4, "score": [3, 2], "series": [[2, 0], [1, 2]]},  # vs Twisted Minds PH
        {"opponent_rank": 5, "score": [3, 3], "series": [[1, 2], [2, 1]]},  # vs TNC Pro Team
        {"opponent_rank": 6, "score": [3, 2], "series": [[1, 2], [2, 0]]},  # vs Team Falcons PH
        {"opponent_rank": 8, "score": [2, 4], "series": [[1, 2], [1, 2]]}   # vs AP.Bren
    ],
    8: [  # AP.Bren
        {"opponent_rank": 1, "score": [1, 4], "series": [[1, 2], [0, 2]]},  # vs Aurora Gaming PH
        {"opponent_rank": 2, "score": [2, 2], "series": [[2, 0], [0, 2]]},  # vs ONIC Philippines
        {"opponent_rank": 3, "score": [0, 4], "series": [[0, 2], [0, 2]]},  # vs Team Liquid PH
        {"opponent_rank": 4, "score": [1, 4], "series": [[0, 2], [1, 2]]},  # vs Twisted Minds PH
        {"opponent_rank": 5, "score": [1, 4], "series": [[1, 2], [0, 2]]},  # vs TNC Pro Team
        {"opponent_rank": 6, "score": [2, 3], "series": [[0, 2], [2, 1]]},  # vs Team Falcons PH
        {"opponent_rank": 7, "score": [4, 2], "series": [[2, 1], [2, 1]]}   # vs Omega Esports
    ]
}

latest_games_win_rate = [
    {
        "rank_id": 1,
        "team": "Aurora Gaming PH",
        "ticker": "RORA",
        "matches_played": 9,
        "series_wins": 9,
        "series_losses": 0,
        "win_match": 18,
        "loss_match": 4,
        "win_series_rate_percentage": 100.0,
        "win_match_rate_percentage": 81.82
    },
    {
        "rank_id": 2,
        "team": "ONIC Philippines",
        "ticker": "ONPH",
        "matches_played": 9,
        "series_wins": 6,
        "series_losses": 3,
        "win_match": 13,
        "loss_match": 9,
        "win_series_rate_percentage": 66.67,
        "win_match_rate_percentage": 59.09
    },
    {
        "rank_id": 3,
        "team": "Team Liquid PH",
        "ticker": "TLPH",
        "matches_played": 9,
        "series_wins": 6,
        "series_losses": 3,
        "win_match": 14,
        "loss_match": 8,
        "win_series_rate_percentage": 66.67,
        "win_match_rate_percentage": 63.64
    },
    {
        "rank_id": 4,
        "team": "Twisted Minds PH",
        "ticker": "TWPH",
        "matches_played": 8,
        "series_wins": 2,
        "series_losses": 6,
        "win_match": 7,
        "loss_match": 13,
        "win_series_rate_percentage": 25.0,
        "win_match_rate_percentage": 35.0
    },
    {
        "rank_id": 5,
        "team": "TNC Pro Team",
        "ticker": "TNC",
        "matches_played": 9,
        "series_wins": 3,
        "series_losses": 6,
        "win_match": 11,
        "loss_match": 14,
        "win_series_rate_percentage": 33.33,
        "win_match_rate_percentage": 44.0
    },
    {
        "rank_id": 6,
        "team": "Team Falcons PH",
        "ticker": "FLCP",
        "matches_played": 8,
        "series_wins": 4,
        "series_losses": 4,
        "win_match": 11,
        "loss_match": 10,
        "win_series_rate_percentage": 50.0,
        "win_match_rate_percentage": 52.38
    },
    {
        "rank_id": 7,
        "team": "Omega Esports",
        "ticker": "OMG",
        "matches_played": 9,
        "series_wins": 3,
        "series_losses": 6,
        "win_match": 8,
        "loss_match": 13,
        "win_series_rate_percentage": 33.33,
        "win_match_rate_percentage": 38.1
    },
    {
        "rank_id": 8,
        "team": "AP.Bren",
        "ticker": "APBR",
        "matches_played": 9,
        "series_wins": 2,
        "series_losses": 7,
        "win_match": 6,
        "loss_match": 14,
        "win_series_rate_percentage": 22.22,
        "win_match_rate_percentage": 30.0
    }
]