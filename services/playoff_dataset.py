from services.matches import (
    get_team_diff,
    get_head_to_head_diff,
    get_latest_match_diff,
)
from pprint import pprint
from services.export import csv

from services.playoff import (
    build_playoff_records_before_bracket,
    build_playoff_features,
)


def remove_unnecessary_dataset_fields(result, target_bracket):
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
            "lower_bracket_appearance_diff",
        ]

    elif target_bracket == "upper_final":
        remove_fields = [
            "upper_series_win_rate_diff",
            "lower_game_win_rate_diff",
            "lower_series_win_rate_diff",
            "lower_bracket_appearance_diff",
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
            "upper_game_win_rate_diff",
        ]

    for base in ["team_a_base", "team_b_base"]:
        for field in remove_fields:
            result[base].pop(field, None)


def generate_playoff_bracket_dataset(
    matchups,
    standings,
    matches,
    target_bracket,
    dataset_name
):
    playoff_records = build_playoff_records_before_bracket(
        matchups,
        target_bracket
    )

    rows = []

    for matchup in matchups:
        if matchup["bracket"] != target_bracket:
            continue

        team_a = matchup["team_a"]
        team_b = matchup["team_b"]

        overall_team_diff = get_team_diff(standings, team_a, team_b)
        head_to_head_diff = get_head_to_head_diff(matches, team_a, team_b)
        latest_match_diff = get_latest_match_diff(matches, team_a, team_b)

        team_a_features = build_playoff_features(
            playoff_records[team_a],
            playoff_records[team_b]
        )

        team_b_features = build_playoff_features(
            playoff_records[team_b],
            playoff_records[team_a]
        )

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

                "win": matchup["is_team_a_win"],
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

                "win": matchup["is_team_b_win"],
            },
        }

        remove_unnecessary_dataset_fields(result, target_bracket)

        rows.append(result["team_a_base"])
        rows.append(result["team_b_base"])
        pprint(f"------ {team_a} vs {team_b} ------")
        pprint(team_a)
        pprint(result["team_a_base"])
        pprint(team_b)
        pprint(result["team_b_base"])

    csv(rows, dataset_name)