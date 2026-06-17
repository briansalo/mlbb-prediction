from collections import defaultdict
from services.matches import get_playoff_records, get_team_records, get_team_diff, get_head_to_head_diff, get_latest_matches_record, get_latest_match_diff
from services.export import csv

def empty_playoff_record():
    return {
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

    playoff_records[team_a]
    playoff_records[team_b]

    is_upper = (
        match.get("is_upper_quarter_final", 0) or
        match.get("is_upper_semi_final", 0) or
        match.get("is_upper_final", 0)
    )

    is_lower = (
        match.get("is_lower_semi_final", 0) or
        match.get("is_lower_final", 0)
    )

    if is_upper:
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




def get_playoff_dataset(
    matchups,
    standings,
    matches,
    preload_stages,
    target_stage,
    dataset_name
):
    playoff_records = defaultdict(empty_playoff_record)

    # 1. Load previous playoff stages first
    for matchup in matchups:
        if any(matchup.get(stage, 0) for stage in preload_stages):
            update_playoff_records(playoff_records, matchup)

    # 2. Generate dataset for target stage
    for matchup in matchups:
        if not matchup.get(target_stage, 0):
            continue

        team_a = matchup["team_a"]
        team_b = matchup["team_b"]
        print([team_a, team_b])
        overall_team_diff = get_team_diff(standings, team_a, team_b)
        head_to_head_diff = get_head_to_head_diff(matches, team_a, team_b)
        latest_match_diff = get_latest_match_diff(matches, team_a, team_b)

        team_a_playoff = playoff_records[team_a]
        team_b_playoff = playoff_records[team_b]

        result = {
            "team_a_base": {
                "overall_game_rank_diff": overall_team_diff["team_a_base"]["rank_diff"],
                "overall_game_win_rate_diff": overall_team_diff["team_a_base"]["game_win_rate_diff"],
                "overall_series_win_rate_diff": overall_team_diff["team_a_base"]["series_win_rate_diff"],

                "head_to_head_game_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_game_win_rate_diff"],
                "head_to_head_series_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_series_win_rate_diff"],

                "latest_series_win_rate_diff": latest_match_diff["team_a_base"]["latest_series_win_rate_percentage_diff"],
                "latest_game_win_rate_diff": latest_match_diff["team_a_base"]["latest_game_win_rate_percentage_diff"],

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

                "upper_game_win_rate_diff": round(
                    team_b_playoff["upper_game_win_rate"] -
                    team_a_playoff["upper_game_win_rate"], 2
                ),
                "upper_series_win_rate_diff": round(
                    team_b_playoff["upper_series_win_rate"] -
                    team_a_playoff["upper_series_win_rate"], 2
                ),

                "lower_game_win_rate_diff": round(
                    team_b_playoff["lower_game_win_rate"] -
                    team_a_playoff["lower_game_win_rate"], 2
                ),
                "lower_series_win_rate_diff": round(
                    team_b_playoff["lower_series_win_rate"] -
                    team_a_playoff["lower_series_win_rate"], 2
                ),

                "win": matchup["is_team_b_win"]
            }
        }

        # removing unecessary fields
        if target_stage == "is_upper_semi_final":
            for team in ["team_a_base", "team_b_base"]:
                del result[team]["upper_series_win_rate_diff"]
                del result[team]["lower_game_win_rate_diff"]
                del result[team]["lower_series_win_rate_diff"]

        elif target_stage == "is_lower_semi_final":
            for team in ["team_a_base", "team_b_base"]:
                del result[team]["lower_game_win_rate_diff"]
                del result[team]["lower_series_win_rate_diff"]

        elif target_stage == "is_upper_final":
            for team in ["team_a_base", "team_b_base"]:
                del result[team]["upper_series_win_rate_diff"]
                del result[team]["lower_game_win_rate_diff"]
                del result[team]["lower_series_win_rate_diff"]
        elif target_stage == "is_lower_final":
            for team in ["team_a_base", "team_b_base"]:
                del result[team]["upper_series_win_rate_diff"]
                del result[team]["lower_series_win_rate_diff"]
        csv([result["team_a_base"], result["team_b_base"]], dataset_name)
