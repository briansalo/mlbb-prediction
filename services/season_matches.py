from collections import defaultdict
from services.matches import get_playoff_records, get_team_records, get_team_diff, get_head_to_head_diff, get_latest_matches_record, get_latest_match_diff
from services.export import csv
from pprint import pprint

def get_season_dataset(matchups, standings, matches, dataset_name):
    for matchup in matchups:
        team_a = matchup["team_a"]
        team_b = matchup["team_b"]

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
        
        # playoff_team_diff = get_playoff_game_win_rate(matchups, team_a, team_b, 'upper_quarter')
        # print("playoff")
        # pprint(playoff_team_diff)
        result = {
            "team_a_base" : {
                "overall_game_rank_diff": overall_team_diff["team_a_base"]["rank_diff"],
                "overall_game_win_rate_diff": overall_team_diff["team_a_base"]["game_win_rate_diff"],
                "overall_series_win_rate_diff": overall_team_diff["team_a_base"]["series_win_rate_diff"],
                "head_to_head_game_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_game_win_rate_diff"],
                "head_to_head_series_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_series_win_rate_diff"],
                "latest_series_win_rate_diff": latest_match_diff["team_a_base"]["latest_series_win_rate_percentage_diff"],
                "latest_game_win_rate_diff": latest_match_diff["team_a_base"]["latest_game_win_rate_percentage_diff"],
                "win": matchup["is_team_a_win"]
            },
            "team_b_base" : {
                "overall_game_rank_diff": overall_team_diff["team_b_base"]["rank_diff"],
                "overall_game_win_rate_diff": overall_team_diff["team_b_base"]["game_win_rate_diff"],
                "overall_series_win_rate_diff": overall_team_diff["team_b_base"]["series_win_rate_diff"],
                "head_to_head_game_win_rate_diff": head_to_head_diff["team_b_base"]["head_to_head_game_win_rate_diff"],
                "head_to_head_series_win_rate_diff": head_to_head_diff["team_b_base"]["head_to_head_series_win_rate_diff"],
                "latest_series_win_rate_diff": latest_match_diff["team_b_base"]["latest_series_win_rate_percentage_diff"],
                "latest_game_win_rate_diff": latest_match_diff["team_b_base"]["latest_game_win_rate_percentage_diff"],
                "win": matchup["is_team_b_win"]
            }
        }
        pprint([team_a, team_b])
        pprint(latest_match_diff)
        csv([result["team_a_base"], result["team_b_base"]], dataset_name)