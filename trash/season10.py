regular_season_standings = [
    {
        "rank": 1,
        "team": "ECHO",
        "match_wins": 10,
        "match_losses": 4,
        "game_wins": 22,
        "game_losses": 13,
        "game_diff": 9,
        "points": 10
    },
    {
        "rank": 2,
        "team": "BLCK",
        "match_wins": 9,
        "match_losses": 5,
        "game_wins": 24,
        "game_losses": 16,
        "game_diff": 8,
        "points": 9
    },
    {
        "rank": 3,
        "team": "RSG",
        "match_wins": 8,
        "match_losses": 6,
        "game_wins": 20,
        "game_losses": 15,
        "game_diff": 5,
        "points": 8
    },
    {
        "rank": 4,
        "team": "BREN",
        "match_wins": 8,
        "match_losses": 6,
        "game_wins": 18,
        "game_losses": 19,
        "game_diff": -1,
        "points": 8
    },
    {
        "rank": 5,
        "team": "ONIC",
        "match_wins": 7,
        "match_losses": 7,
        "game_wins": 16,
        "game_losses": 21,
        "game_diff": -5,
        "points": 7
    },
    {
        "rank": 6,
        "team": "OMG",
        "match_wins": 6,
        "match_losses": 8,
        "game_wins": 14,
        "game_losses": 18,
        "game_diff": -4,
        "points": 6
    },
    {
        "rank": 7,
        "team": "NXPE",
        "match_wins": 3,
        "match_losses": 11,
        "game_wins": 9,
        "game_losses": 29,
        "game_diff": -20,
        "points": 3
    },
    {
        "rank": 8,
        "team": "TNC",
        "match_wins": 1,
        "match_losses": 13,
        "game_wins": 7,
        "game_losses": 22,
        "game_diff": -15,
        "points": 1
    }
]

head_to_head_data = {
    1: [  # ECHO
        {"opponent_rank": 2, "win": 2, "loss": 3, "series": [[2, 1], [0, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 3, "win": 1, "loss": 4, "series": [[0, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 4, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 5, "win": 3, "loss": 2, "series": [[1, 2], [2, 0]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 6, "win": 4, "loss": 2, "series": [[2, 1], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 7, "win": 4, "loss": 1, "series": [[2, 1], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 4, "loss": 1, "series": [[2, 1], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    2: [  # BLCK
        {"opponent_rank": 1, "win": 3, "loss": 2, "series": [[1, 2], [2, 0]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 3, "win": 3, "loss": 2, "series": [[2, 0], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 4, "win": 4, "loss": 2, "series": [[2, 1], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 5, "win": 4, "loss": 1, "series": [[2, 0], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 6, "win": 3, "loss": 3, "series": [[2, 1], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 7, "win": 4, "loss": 1, "series": [[2, 1], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 4, "loss": 1, "series": [[2, 1], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    3: [  # RSG PH
        {"opponent_rank": 1, "win": 4, "loss": 1, "series": [[2, 0], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 2, "win": 2, "loss": 3, "series": [[0, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 4, "win": 2, "loss": 3, "series": [[0, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 5, "win": 3, "loss": 3, "series": [[0, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 6, "win": 3, "loss": 2, "series": [[1, 2], [2, 0]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 7, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 2, "loss": 2, "series": [[2, 0], [0, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
    ],

    4: [  # Bren
        {"opponent_rank": 1, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 2, "loss": 4, "series": [[1, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 3, "win": 3, "loss": 2, "series": [[2, 0], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 5, "win": 3, "loss": 3, "series": [[2, 1], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 6, "win": 4, "loss": 2, "series": [[2, 1], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 7, "win": 4, "loss": 1, "series": [[2, 0], [2, 1]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    5: [  # OMG
        {"opponent_rank": 1, "win": 2, "loss": 3, "series": [[2, 1], [0, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 2, "win": 1, "loss": 4, "series": [[0, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 3, "win": 3, "loss": 3, "series": [[2, 0], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 4, "win": 3, "loss": 3, "series": [[1, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 6, "win": 3, "loss": 2, "series": [[2, 0], [1, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 7, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 2, "loss": 1, "series": [[2, 1], [0, 0]], "series_win": 1, "series_loss": 0, "series_win_rate": 100.0},
    ],

    6: [  # ONIC
        {"opponent_rank": 1, "win": 2, "loss": 4, "series": [[1, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 3, "loss": 3, "series": [[1, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 3, "win": 2, "loss": 3, "series": [[2, 1], [0, 2]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 4, "win": 2, "loss": 4, "series": [[1, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 5, "win": 2, "loss": 3, "series": [[0, 2], [2, 1]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 7, "win": 3, "loss": 0, "series": [[2, 0], [1, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
        {"opponent_rank": 8, "win": 4, "loss": 0, "series": [[2, 0], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    7: [  # NXPE
        {"opponent_rank": 1, "win": 1, "loss": 4, "series": [[1, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 1, "loss": 4, "series": [[1, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 3, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 4, "win": 1, "loss": 4, "series": [[0, 2], [1, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 5, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 6, "win": 0, "loss": 3, "series": [[0, 2], [0, 1]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 8, "win": 4, "loss": 1, "series": [[2, 1], [2, 0]], "series_win": 2, "series_loss": 0, "series_win_rate": 100.0},
    ],

    8: [  # TNC
        {"opponent_rank": 1, "win": 1, "loss": 4, "series": [[1, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 2, "win": 1, "loss": 4, "series": [[1, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 3, "win": 2, "loss": 2, "series": [[0, 2], [2, 0]], "series_win": 1, "series_loss": 1, "series_win_rate": 50.0},
        {"opponent_rank": 4, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 5, "win": 1, "loss": 2, "series": [[1, 2], [0, 0]], "series_win": 0, "series_loss": 1, "series_win_rate": 0.0},
        {"opponent_rank": 6, "win": 0, "loss": 4, "series": [[0, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
        {"opponent_rank": 7, "win": 1, "loss": 4, "series": [[1, 2], [0, 2]], "series_win": 0, "series_loss": 2, "series_win_rate": 0.0},
    ],
}