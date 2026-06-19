from services.matches import get_team_diff, get_head_to_head_diff, get_latest_matches_record, get_latest_match_diff
from pprint import pprint
from services.playoffs_matches import get_playoff_diff
def predict_matchup(matchups, model_name, standings, matches, team_a, team_b, matchup):
    overall_team_diff = get_team_diff(
        standings,
        team_a,
        team_b
    )


    head_to_head_diff = get_head_to_head_diff(
        matches,
        team_a,
        team_b
    )
    latest_match_diff = get_latest_match_diff(
        matches,
        team_a,
        team_b
    )
    
    test = get_playoff_diff(
        matchups,
        team_a,
        team_b,
        matchup["bracket"]
    )
    print("-----test----------")
    print(test)

    if "face_off" in model_name:
        return [
            overall_team_diff["team_a_base"]["rank_diff"],
            overall_team_diff["team_a_base"]["game_win_rate_diff"],
            overall_team_diff["team_a_base"]["series_win_rate_diff"],
            head_to_head_diff["team_a_base"]["head_to_head_game_win_rate_diff"],
            head_to_head_diff["team_a_base"]["head_to_head_series_win_rate_diff"],
            latest_match_diff["team_a_base"]["latest_series_win_rate_percentage_diff"],
            latest_match_diff["team_a_base"]["latest_game_win_rate_percentage_diff"],
        ]

    
