from collections import defaultdict
from pprint import pprint

from services.matches import (
    get_team_diff,
    get_head_to_head_diff,
    get_latest_match_diff,
)
from services.export import csv


UPPER_BRACKETS = [
    "upper_quarter_final",
    "upper_semi_final",
    "upper_final",
]

LOWER_BRACKETS = [
    "lower_semi_final",
    "lower_final",
]

PRELOAD_BRACKETS = {
    "upper_semi_final": [
        "upper_quarter_final",
    ],

    "upper_final": [
        "upper_quarter_final",
        "upper_semi_final",
    ],

    "lower_semi_final": [
        "upper_quarter_final",
        "upper_semi_final",
    ],

    "lower_final": [
        "upper_quarter_final",
        "upper_semi_final",
        "upper_final",
        "lower_semi_final",
    ],

    "grand_final": [
        "upper_quarter_final",
        "upper_semi_final",
        "upper_final",
        "lower_semi_final",
        "lower_final",
    ],
}


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

    playoff_records[team_a]
    playoff_records[team_b]

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


def get_playoff_records_before_bracket(matchups, target_bracket):
    playoff_records = defaultdict(empty_playoff_record)

    preload_brackets = PRELOAD_BRACKETS.get(target_bracket, [])

    for matchup in matchups:
        if matchup["bracket"] in preload_brackets:
            update_playoff_records(playoff_records, matchup)

    return playoff_records


def get_playoff_diff(matchups, team_a, team_b, target_bracket):
    records = get_playoff_records_before_bracket(matchups, target_bracket)

    a = records[team_a]
    b = records[team_b]

    result = {
        "upper_bracket_appearance_diff": (
            a["upper_bracket_appearance"] -
            b["upper_bracket_appearance"]
        ),

        "lower_bracket_appearance_diff": (
            a["lower_bracket_appearance"] -
            b["lower_bracket_appearance"]
        ),

        "upper_game_win_rate_diff": round(
            a["upper_game_win_rate"] -
            b["upper_game_win_rate"], 2
        ),

        "upper_series_win_rate_diff": round(
            a["upper_series_win_rate"] -
            b["upper_series_win_rate"], 2
        ),

        "lower_game_win_rate_diff": round(
            a["lower_game_win_rate"] -
            b["lower_game_win_rate"], 2
        ),

        "lower_series_win_rate_diff": round(
            a["lower_series_win_rate"] -
            b["lower_series_win_rate"], 2
        ),
    }

    return remove_unnecessary_playoff_fields(
        result,
        target_bracket
    )

def remove_unnecessary_playoff_fields(result, target_bracket):
    if target_bracket == "upper_semi_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_bracket_appearance_diff",
            "lower_game_win_rate_diff",
            "lower_series_win_rate_diff",
        ]

    elif target_bracket == "lower_semi_final":
        remove_fields = [
            "lower_game_win_rate_diff",
            "lower_series_win_rate_diff",
            "upper_series_win_rate_diff",
            "lower_bracket_appearance_diff"
        ]

    elif target_bracket == "upper_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_game_win_rate_diff",
            "lower_series_win_rate_diff",
            "lower_bracket_appearance_diff"
        ]

    elif target_bracket == "lower_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_series_win_rate_diff",
        ]
    elif target_bracket == "grand_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_series_win_rate_diff",
        ]
    else:
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_series_win_rate_diff",
            "lower_game_win_rate_diff",
            "upper_game_win_rate_diff"
        ]

    for field in remove_fields:
        result.pop(field, None)

    return result

def remove_unnecessary_fields(result, target_bracket):
    if target_bracket == "upper_semi_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_bracket_appearance_diff",
            "lower_game_win_rate_diff",
            "lower_series_win_rate_diff",
        ]

    elif target_bracket == "lower_semi_final":
        remove_fields = [
            "lower_game_win_rate_diff",
            "lower_series_win_rate_diff",
            "upper_series_win_rate_diff",
            "lower_bracket_appearance_diff"
        ]

    elif target_bracket == "upper_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_game_win_rate_diff",
            "lower_series_win_rate_diff",
            "lower_bracket_appearance_diff"
        ]

    elif target_bracket == "lower_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_series_win_rate_diff",
        ]
    elif target_bracket == "grand_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_series_win_rate_diff",
        ]
    else:
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_series_win_rate_diff",
            "lower_game_win_rate_diff",
            "upper_game_win_rate_diff"
        ]

    for base in ["team_a_base", "team_b_base"]:
        for field in remove_fields:
            result[base].pop(field, None)


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


def get_playoff_dataset(
    matchups,
    standings,
    matches,
    preload_brackets,
    target_bracket,
    dataset_name
):
    playoff_records = defaultdict(empty_playoff_record)

    for matchup in matchups:
        if matchup["bracket"] in preload_brackets:
            update_playoff_records(playoff_records, matchup)

    for matchup in matchups:
        if matchup["bracket"] != target_bracket:
            continue

        team_a = matchup["team_a"]
        team_b = matchup["team_b"]

        print([team_a, team_b])

        overall_team_diff = get_team_diff(standings, team_a, team_b)
        head_to_head_diff = get_head_to_head_diff(matches, team_a, team_b)
        latest_match_diff = get_latest_match_diff(matches, team_a, team_b)

        team_a_playoff = playoff_records[team_a]
        team_b_playoff = playoff_records[team_b]

        team_a_features = build_playoff_features(team_a_playoff, team_b_playoff)
        team_b_features = build_playoff_features(team_b_playoff, team_a_playoff)

        result = {
            "team_a_base": {
                "overall_game_rank_diff": overall_team_diff["team_a_base"]["rank_diff"],
                "overall_game_win_rate_diff": overall_team_diff["team_a_base"]["game_win_rate_diff"],
                "overall_series_win_rate_diff": overall_team_diff["team_a_base"]["series_win_rate_diff"],

                "head_to_head_game_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_game_win_rate_diff"],
                "head_to_head_series_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_series_win_rate_diff"],

                "latest_series_win_rate_diff": latest_match_diff["team_a_base"]["latest_series_win_rate_percentage_diff"],
                "latest_game_win_rate_diff": latest_match_diff["team_a_base"]["latest_game_win_rate_percentage_diff"],

                **team_a_features,

                "win": matchup["is_team_a_win"]
            },

            "team_b_base": {
                "overall_game_rank_diff": overall_team_diff["team_b_base"]["rank_diff"],
                "overall_game_win_rate_diff": overall_team_diff["team_b_base"]["game_win_rate_diff"],
                "overall_series_win_rate_diff": overall_team_diff["team_b_base"]["series_win_rate_diff"],

                "head_to_head_game_win_rate_diff": head_to_head_diff["team_b_base"]["head_to_head_game_win_rate_diff"],
                "head_to_head_series_win_rate_diff": head_to_head_diff["team_b_base"]["head_to_head_series_win_rate_diff"],

                "latest_series_win_rate_diff": latest_match_diff["team_b_base"]["latest_series_win_rate_percentage_diff"],
                "latest_game_win_rate_diff": latest_match_diff["team_b_base"]["latest_game_win_rate_percentage_diff"],

                **team_b_features,

                "win": matchup["is_team_b_win"]
            }
        }

        remove_unnecessary_fields(result, target_bracket)

        pprint(result["team_a_base"])
        pprint(result["team_b_base"])

        csv([result["team_a_base"], result["team_b_base"]], dataset_name)