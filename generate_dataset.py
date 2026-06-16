
from services.matches import get_playoff_records, get_team_records, get_team_diff, get_head_to_head_diff, get_latest_matches_record, get_latest_match_diff
from services.input import prompt_compare
from services.export import csv
from pprint import pprint
from data.matchups.id.season_14 import matchups
from data.matches.id.id_season_14_matches import matches
from data.matchups.id.season_4 import matchups as season_4_matchups
from data.matchups.id.season_5 import matchups as season_5_matchups
from data.matchups.id.season_6 import matchups as season_6_matchups
from data.matchups.id.season_7 import matchups as season_7_matchups
from data.matchups.id.season_8 import matchups as season_8_matchups
from data.matchups.id.season_9 import matchups as season_9_matchups
from data.matchups.id.season_10 import matchups as season_10_matchups
from data.matchups.id.season_11 import matchups as season_11_matchups
from data.matchups.id.season_12 import matchups as season_12_matchups
from data.matchups.id.season_13 import matchups as season_13_matchups
from data.matchups.id.season_14 import matchups as season_14_matchups

from data.matches.id.id_season_4_matches import matches as season_4_matches
from data.matches.id.id_season_5_matches import matches as season_5_matches
from data.matches.id.id_season_6_matches import matches as season_6_matches
from data.matches.id.id_season_7_matches import matches as season_7_matches
from data.matches.id.id_season_8_matches import matches as season_8_matches
from data.matches.id.id_season_9_matches import matches as season_9_matches
from data.matches.id.id_season_10_matches import matches as season_10_matches
from data.matches.id.id_season_11_matches import matches as season_11_matches
from data.matches.id.id_season_12_matches import matches as season_12_matches
from data.matches.id.id_season_13_matches import matches as season_13_matches
from data.matches.id.id_season_14_matches import matches as season_14_matches

seasons = [
    (season_4_matchups, season_4_matches),
    # (season_5_matchups, season_5_matches),
    # (season_6_matchups, season_6_matches),
    # (season_7_matchups, season_7_matches),
    # (season_8_matchups, season_8_matches),
    # (season_9_matchups, season_9_matches),
    # (season_10_matchups, season_10_matches),
    # (season_11_matchups, season_11_matches),
    # (season_12_matchups, season_12_matches),
    # (season_13_matchups, season_13_matches),
    # (season_14_matchups, season_14_matches)
]


def get_matchups(matchups, standings, matches):
    dataset_name = "datasets/ml_dataset-id-s14-rate.csv"
          


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

        if "rate" in dataset_name:
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
        else:
            result = {
                "team_a_base" : {
                    "overall_rank_diff": overall_team_diff["team_a_base"]["rank_diff"],
                    "overall_series_win_diff": overall_team_diff["team_a_base"]["series_win_diff"],
                    "overall_series_loss_diff": overall_team_diff["team_a_base"]["series_loss_diff"],
                    "overall_game_win_diff": overall_team_diff["team_a_base"]["game_win_diff"],
                    "overall_game_loss_diff": overall_team_diff["team_a_base"]["game_loss_diff"],
                    "head_to_head_game_win": head_to_head_diff["team_a_base"]["head_to_head_game_win"],
                    "head_to_head_game_loss": head_to_head_diff["team_a_base"]["head_to_head_game_loss"],
                    "head_to_head_series_win": head_to_head_diff["team_a_base"]["head_to_head_series_win"],
                    "head_to_head_series_loss": head_to_head_diff["team_a_base"]["head_to_head_series_loss"],
                    "latest_game_win_diff": latest_match_diff["team_a_base"]["latest_game_win_diff"],
                    "latest_game_loss_diff": latest_match_diff["team_a_base"]["latest_game_loss_diff"],
                    "latest_series_win_diff": latest_match_diff["team_a_base"]["latest_series_win_diff"],
                    "latest_series_loss_diff": latest_match_diff["team_a_base"]["latest_series_loss_diff"],
                    "playoff_h2h_win": 0,
                    "playoff_h2h_loss": 0,
                    "playoff_upper_bracket_win_diff": 0,
                    "playoff_lower_bracket_win_diff": 0,
                    "is_grand_final":0,
                    "win": matchup["is_team_a_win"]
                },
                "team_b_base" : {
                    "overall_rank_diff": overall_team_diff["team_b_base"]["rank_diff"],
                    "overall_series_win_diff": overall_team_diff["team_b_base"]["series_win_diff"],
                    "overall_series_loss_diff": overall_team_diff["team_b_base"]["series_loss_diff"],
                    "overall_game_win_diff": overall_team_diff["team_b_base"]["game_win_diff"],
                    "overall_game_loss_diff": overall_team_diff["team_b_base"]["game_loss_diff"],
                    "head_to_head_game_win": head_to_head_diff["team_b_base"]["head_to_head_game_win"],
                    "head_to_head_game_loss": head_to_head_diff["team_b_base"]["head_to_head_game_loss"],
                    "head_to_head_series_win": head_to_head_diff["team_b_base"]["head_to_head_series_win"],
                    "head_to_head_series_loss": head_to_head_diff["team_b_base"]["head_to_head_series_loss"],
                    "latest_game_win_diff": latest_match_diff["team_b_base"]["latest_game_win_diff"],
                    "latest_game_loss_diff": latest_match_diff["team_b_base"]["latest_game_loss_diff"],
                    "latest_series_win_diff": latest_match_diff["team_b_base"]["latest_series_win_diff"],
                    "latest_series_loss_diff": latest_match_diff["team_b_base"]["latest_series_loss_diff"],
                    "playoff_h2h_win": 0,
                    "playoff_h2h_loss": 0,
                    "playoff_upper_bracket_win_diff": 0,
                    "playoff_lower_bracket_win_diff": 0,
                    "is_grand_final":0,
                    "win": matchup["is_team_b_win"]
                }
            }
        pprint([team_a, team_b])
        pprint(latest_match_diff)
        csv([result["team_a_base"], result["team_b_base"]], dataset_name)


for index, (matchups, matches) in enumerate(seasons, start=1):
    standings = get_team_records(matches)
    get_matchups(matchups, standings, matches)
    print(f" Season #{index}")

