from services.matches import (
    get_team_diff,
    get_head_to_head_diff,
    get_latest_match_diff,
)

from services.playoff import (
    build_playoff_records_before_bracket,
    build_playoff_features,
)


def remove_unnecessary_prediction_fields(result, target_bracket):
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

    for field in remove_fields:
        result.pop(field, None)

    return result


def get_playoff_diff(matchups, team_a, team_b, target_bracket):
    playoff_records = build_playoff_records_before_bracket(
        matchups,
        target_bracket
    )

    result = build_playoff_features(
        playoff_records[team_a],
        playoff_records[team_b]
    )

    return remove_unnecessary_prediction_fields(
        result,
        target_bracket
    )


def predict_playoff_matchup(
    matchups,
    standings,
    matches,
    team_a,
    team_b,
    target_bracket
):
    overall_team_diff = get_team_diff(standings, team_a, team_b)
    head_to_head_diff = get_head_to_head_diff(matches, team_a, team_b)
    latest_match_diff = get_latest_match_diff(matches, team_a, team_b)

    playoff_diff = get_playoff_diff(
        matchups,
        team_a,
        team_b,
        target_bracket
    )

    return {
        "overall_game_rank_diff": overall_team_diff["team_a_base"]["rank_diff"],
        "overall_game_win_rate_diff": overall_team_diff["team_a_base"]["game_win_rate_diff"],
        "overall_series_win_rate_diff": overall_team_diff["team_a_base"]["series_win_rate_diff"],

        "head_to_head_game_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_game_win_rate_diff"],
        "head_to_head_series_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_series_win_rate_diff"],

        "latest_series_win_rate_diff": latest_match_diff["team_a_base"]["latest_series_win_rate_percentage_diff"],
        "latest_game_win_rate_diff": latest_match_diff["team_a_base"]["latest_game_win_rate_percentage_diff"],

        **playoff_diff,
    }