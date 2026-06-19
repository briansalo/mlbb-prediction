from collections import defaultdict

from services.constants import (
    UPPER_BRACKETS,
    LOWER_BRACKETS,
    PRELOAD_BRACKETS,
)


def empty_playoff_record():
    return {
        "upper_bracket_appearance": 0,
        "lower_bracket_appearance": 0,

        "upper_game_win": 0,
        "upper_game_loss": 0,
        "upper_series_win": 0,
        "upper_series_loss": 0,
        "upper_game_win_rate": 0,
        "upper_series_win_rate": 0,

        "lower_game_win": 0,
        "lower_game_loss": 0,
        "lower_series_win": 0,
        "lower_series_loss": 0,
        "lower_game_win_rate": 0,
        "lower_series_win_rate": 0,
    }


def calculate_rate(win, loss):
    total = win + loss
    return round((win / total) * 100, 2) if total else 0


def update_rates(record):
    record["upper_game_win_rate"] = calculate_rate(
        record["upper_game_win"],
        record["upper_game_loss"]
    )

    record["upper_series_win_rate"] = calculate_rate(
        record["upper_series_win"],
        record["upper_series_loss"]
    )

    record["lower_game_win_rate"] = calculate_rate(
        record["lower_game_win"],
        record["lower_game_loss"]
    )

    record["lower_series_win_rate"] = calculate_rate(
        record["lower_series_win"],
        record["lower_series_loss"]
    )


def update_playoff_records(playoff_records, match):
    team_a = match["team_a"]
    team_b = match["team_b"]

    team_a_score = match["team_a_score"]
    team_b_score = match["team_b_score"]
    bracket = match["bracket"]

    is_upper = bracket in UPPER_BRACKETS
    is_lower = bracket in LOWER_BRACKETS

    if is_upper:
        playoff_records[team_a]["upper_bracket_appearance"] += 1
        playoff_records[team_b]["upper_bracket_appearance"] += 1

        playoff_records[team_a]["upper_game_win"] += team_a_score
        playoff_records[team_a]["upper_game_loss"] += team_b_score

        playoff_records[team_b]["upper_game_win"] += team_b_score
        playoff_records[team_b]["upper_game_loss"] += team_a_score

        if match["is_team_a_win"]:
            playoff_records[team_a]["upper_series_win"] += 1
            playoff_records[team_b]["upper_series_loss"] += 1
        else:
            playoff_records[team_b]["upper_series_win"] += 1
            playoff_records[team_a]["upper_series_loss"] += 1

    elif is_lower:
        playoff_records[team_a]["lower_bracket_appearance"] += 1
        playoff_records[team_b]["lower_bracket_appearance"] += 1

        playoff_records[team_a]["lower_game_win"] += team_a_score
        playoff_records[team_a]["lower_game_loss"] += team_b_score

        playoff_records[team_b]["lower_game_win"] += team_b_score
        playoff_records[team_b]["lower_game_loss"] += team_a_score

        if match["is_team_a_win"]:
            playoff_records[team_a]["lower_series_win"] += 1
            playoff_records[team_b]["lower_series_loss"] += 1
        else:
            playoff_records[team_b]["lower_series_win"] += 1
            playoff_records[team_a]["lower_series_loss"] += 1

    update_rates(playoff_records[team_a])
    update_rates(playoff_records[team_b])


def build_playoff_records_before_bracket(matchups, target_bracket):
    playoff_records = defaultdict(empty_playoff_record)

    preload_brackets = PRELOAD_BRACKETS.get(target_bracket, [])

    for matchup in matchups:
        if matchup["bracket"] in preload_brackets:
            update_playoff_records(playoff_records, matchup)

    return playoff_records


def build_playoff_features(team_a_playoff, team_b_playoff):
    return {
        "upper_bracket_appearance_diff": (
            team_a_playoff["upper_bracket_appearance"] -
            team_b_playoff["upper_bracket_appearance"]
        ),

        "lower_bracket_appearance_diff": (
            team_a_playoff["lower_bracket_appearance"] -
            team_b_playoff["lower_bracket_appearance"]
        ),

        "upper_game_win_rate_diff": round(
            team_a_playoff["upper_game_win_rate"] -
            team_b_playoff["upper_game_win_rate"], 2
        ),

        "upper_series_win_rate_diff": round(
            team_a_playoff["upper_series_win_rate"] -
            team_b_playoff["upper_series_win_rate"], 2
        ),

        "lower_game_win_rate_diff": round(
            team_a_playoff["lower_game_win_rate"] -
            team_b_playoff["lower_game_win_rate"], 2
        ),

        "lower_series_win_rate_diff": round(
            team_a_playoff["lower_series_win_rate"] -
            team_b_playoff["lower_series_win_rate"], 2
        ),
    }