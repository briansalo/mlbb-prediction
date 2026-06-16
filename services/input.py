from services.matches import get_team_records, get_team_diff, get_head_to_head_diff, get_latest_match_diff
from services.export import csv
from pprint import pprint
def prompt_compare(matches):
    team_a = input("Team A ticker: ").strip().upper()
    team_b = input("Team B ticker: ").strip().upper()

    standings = get_team_records(matches)

    overall = get_team_diff(
        standings,
        team_a,
        team_b
    )

    h2h = get_head_to_head_diff(
        matches,
        team_a,
        team_b
    )
    latest = get_latest_match_diff(
        matches,
        team_a,
        team_b)

    # pprint("\n=== OVERALL ===")
    # pprint(overall)

    # pprint("\n=== HEAD TO HEAD ===")
    # pprint(h2h)
    # pprint("\n=== LATEST ===")
    # pprint(latest)
    # row = {
    #     **overall,
    #     **h2h,
    #     **latest
    # }
    row ={
        "overall_rank_diff": overall["rank_diff"],
        "overall_series_win_diff": overall["series_win_diff"],
        "overall_series_loss_diff": overall["series_loss_diff"],
        "overall_game_win_diff": overall["game_win_diff"],
        "overall_game_loss_diff": overall["game_loss_diff"],
        "head_to_head_game_win": h2h["head_to_head_game_win"],
        "head_to_head_game_loss": h2h["head_to_head_game_loss"],
        "head_to_head_series_win": h2h["head_to_head_series_win"],
        "head_to_head_series_loss": h2h["head_to_head_series_loss"],
        "latest_game_win_diff": latest["latest_game_win_diff"],
        "latest_game_loss_diff": latest["latest_game_loss_diff"],
        "latest_series_win_diff": latest["latest_series_win_diff"],
        "latest_series_loss_diff": latest["latest_series_loss_diff"],
        "playoff_h2h_win": 0,
        "playoff_h2h_loss": 0,
        "playoff_upper_bracket_win_diff": 0,
        "playoff_lower_bracket_win_diff": 0,
        "is_grand_final":0,
        "win": 1
    }

    csv([row], "ml_dataset.csv")