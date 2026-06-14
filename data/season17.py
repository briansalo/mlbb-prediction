regular_season_standings = [
    {
        "rank": 1,
        "team": "TLPH",
        "match_wins": 13,
        "match_losses": 1,
        "game_wins": 27,
        "game_losses": 6,
        "game_diff": 21,
        "points": 13
    },
    {
        "rank": 2,
        "team": "FLCP",
        "match_wins": 12,
        "match_losses": 2,
        "game_wins": 26,
        "game_losses": 8,
        "game_diff": 18,
        "points": 12
    },
    {
        "rank": 3,
        "team": "ONPH",
        "match_wins": 9,
        "match_losses": 5,
        "game_wins": 20,
        "game_losses": 13,
        "game_diff": 7,
        "points": 9
    },
    {
        "rank": 4,
        "team": "OMG",
        "match_wins": 6,
        "match_losses": 8,
        "game_wins": 15,
        "game_losses": 19,
        "game_diff": -4,
        "points": 6
    },
    {
        "rank": 5,
        "team": "TWPH",
        "match_wins": 6,
        "match_losses": 8,
        "game_wins": 13,
        "game_losses": 20,
        "game_diff": -7,
        "points": 6
    },
    {
        "rank": 6,
        "team": "RORA",
        "match_wins": 5,
        "match_losses": 9,
        "game_wins": 15,
        "game_losses": 20,
        "game_diff": -5,
        "points": 5
    },
    {
        "rank": 7,
        "team": "APBR",
        "match_wins": 3,
        "match_losses": 11,
        "game_wins": 10,
        "game_losses": 24,
        "game_diff": -14,
        "points": 3
    },
    {
        "rank": 8,
        "team": "TNC",
        "match_wins": 2,
        "match_losses": 12,
        "game_wins": 8,
        "game_losses": 24,
        "game_diff": -16,
        "points": 2
    }
]


head_to_head_data = {
    1: [  # TLPH
        {"opponent_rank": 2, "win": 3, "loss": 3, "series": [[2, 1], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 3, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 4, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 5, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 6, "win": 4, "loss": 1, "series": [[2, 1], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 7, "win": 4, "loss": 2, "series": [[2, 1], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    2: [  # FLCP
        {"opponent_rank": 1, "win": 3, "loss": 3, "series": [[1, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 3, "win": 4, "loss": 2, "series": [[2, 1], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 4, "win": 3, "loss": 2, "series": [[2, 0], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 5, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 6, "win": 4, "loss": 1, "series": [[2, 1], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 7, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    3: [  # ONPH
        {"opponent_rank": 1, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 2, "loss": 4, "series": [[1, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 4, "win": 4, "loss": 1, "series": [[2, 0], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 5, "win": 4, "loss": 1, "series": [[2, 1], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 6, "win": 4, "loss": 1, "series": [[2, 0], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 7, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 2, "loss": 2, "series": [[0, 2], [2, 0]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
    ],

    4: [  # OMG
        {"opponent_rank": 1, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 2, "loss": 3, "series": [[0, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 3, "win": 1, "loss": 4, "series": [[0, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 5, "win": 3, "loss": 2, "series": [[1, 2], [2, 0]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 6, "win": 3, "loss": 3, "series": [[2, 1], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 7, "win": 2, "loss": 3, "series": [[0, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 8, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    5: [  # TWPH
        {"opponent_rank": 1, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 3, "win": 1, "loss": 4, "series": [[1, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 4, "win": 2, "loss": 3, "series": [[2, 1], [0, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 6, "win": 2, "loss": 3, "series": [[0, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 7, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 4, "loss": 2, "series": [[2, 1], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    6: [  # RORA
        {"opponent_rank": 1, "win": 1, "loss": 4, "series": [[1, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 1, "loss": 4, "series": [[1, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 3, "win": 1, "loss": 4, "series": [[0, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 4, "win": 3, "loss": 3, "series": [[1, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 5, "win": 3, "loss": 2, "series": [[2, 0], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 7, "win": 4, "loss": 1, "series": [[2, 0], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 2, "loss": 2, "series": [[2, 0], [0, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
    ],

    7: [  # APBR
        {"opponent_rank": 1, "win": 2, "loss": 4, "series": [[1, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 3, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 4, "win": 3, "loss": 2, "series": [[2, 0], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 5, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 6, "win": 1, "loss": 4, "series": [[0, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 8, "win": 4, "loss": 2, "series": [[2, 1], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    8: [  # TNC
        {"opponent_rank": 1, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 3, "win": 2, "loss": 2, "series": [[2, 0], [0, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 4, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 5, "win": 2, "loss": 4, "series": [[1, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 6, "win": 2, "loss": 2, "series": [[0, 2], [2, 0]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 7, "win": 2, "loss": 4, "series": [[1, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
    ],
}

latest_games_win_rate = [
    {"rank_id": 1, "team": "Team Liquid PH", "ticker": "TLPH", "matches_played": 7, "series_wins": 6, "series_losses": 1, "win_match": 13, "loss_match": 3, "win_series_rate_percentage": 85.71, "win_match_rate_percentage": 81.25},
    {"rank_id": 2, "team": "Team Falcons PH", "ticker": "FLCP", "matches_played": 7, "series_wins": 6, "series_losses": 1, "win_match": 13, "loss_match": 4, "win_series_rate_percentage": 85.71, "win_match_rate_percentage": 76.47},
    {"rank_id": 3, "team": "ONIC Philippines", "ticker": "ONPH", "matches_played": 7, "series_wins": 5, "series_losses": 2, "win_match": 11, "loss_match": 6, "win_series_rate_percentage": 71.43, "win_match_rate_percentage": 64.71},
    {"rank_id": 4, "team": "Omega Esports", "ticker": "OMG", "matches_played": 7, "series_wins": 4, "series_losses": 3, "win_match": 10, "loss_match": 8, "win_series_rate_percentage": 57.14, "win_match_rate_percentage": 55.56},
    {"rank_id": 5, "team": "Twisted Minds PH", "ticker": "TWPH", "matches_played": 7, "series_wins": 3, "series_losses": 4, "win_match": 6, "loss_match": 10, "win_series_rate_percentage": 42.86, "win_match_rate_percentage": 37.5},
    {"rank_id": 6, "team": "Aurora Gaming PH", "ticker": "RORA", "matches_played": 7, "series_wins": 2, "series_losses": 5, "win_match": 6, "loss_match": 12, "win_series_rate_percentage": 28.57, "win_match_rate_percentage": 33.33},
    {"rank_id": 7, "team": "AP.Bren", "ticker": "APBR", "matches_played": 7, "series_wins": 1, "series_losses": 6, "win_match": 5, "loss_match": 13, "win_series_rate_percentage": 14.29, "win_match_rate_percentage": 27.78},
    {"rank_id": 8, "team": "TNC Pro Team", "ticker": "TNC", "matches_played": 7, "series_wins": 1, "series_losses": 6, "win_match": 4, "loss_match": 12, "win_series_rate_percentage": 14.29, "win_match_rate_percentage": 25.0},
]