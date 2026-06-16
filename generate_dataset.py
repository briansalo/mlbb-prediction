from data.matches.id.id_season_10_matches import matches
from services.matches import get_team_records, get_team_diff, get_head_to_head_diff, get_latest_matches_record, get_latest_match_diff
from services.input import prompt_compare
from services.export import csv
from pprint import pprint
from data.matchups.id.season_10 import matchups


standings = get_team_records(matches)
def get_matchups(matchups, standings, matches):
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
        # result = {
        #     "team_a_base" : {
        #         "overall_rank_diff": overall_team_diff["team_a_base"]["rank_diff"],
        #         "overall_series_win_diff": overall_team_diff["team_a_base"]["series_win_diff"],
        #         "overall_series_loss_diff": overall_team_diff["team_a_base"]["series_loss_diff"],
        #         "overall_game_win_diff": overall_team_diff["team_a_base"]["game_win_diff"],
        #         "overall_game_loss_diff": overall_team_diff["team_a_base"]["game_loss_diff"],
        #         "head_to_head_game_win": head_to_head_diff["team_a_base"]["head_to_head_game_win"],
        #         "head_to_head_game_loss": head_to_head_diff["team_a_base"]["head_to_head_game_loss"],
        #         "head_to_head_series_win": head_to_head_diff["team_a_base"]["head_to_head_series_win"],
        #         "head_to_head_series_loss": head_to_head_diff["team_a_base"]["head_to_head_series_loss"],
        #         "latest_game_win_diff": latest_match_diff["team_a_base"]["latest_game_win_diff"],
        #         "latest_game_loss_diff": latest_match_diff["team_a_base"]["latest_game_loss_diff"],
        #         "latest_series_win_diff": latest_match_diff["team_a_base"]["latest_series_win_diff"],
        #         "latest_series_loss_diff": latest_match_diff["team_a_base"]["latest_series_loss_diff"],
        #         "playoff_h2h_win": 0,
        #         "playoff_h2h_loss": 0,
        #         "playoff_upper_bracket_win_diff": 0,
        #         "playoff_lower_bracket_win_diff": 0,
        #         "is_grand_final":0,
        #         "win": matchup["is_team_a_win"]
        #     },
        #     "team_b_base" : {
        #         "overall_rank_diff": overall_team_diff["team_b_base"]["rank_diff"],
        #         "overall_series_win_diff": overall_team_diff["team_b_base"]["series_win_diff"],
        #         "overall_series_loss_diff": overall_team_diff["team_b_base"]["series_loss_diff"],
        #         "overall_game_win_diff": overall_team_diff["team_b_base"]["game_win_diff"],
        #         "overall_game_loss_diff": overall_team_diff["team_b_base"]["game_loss_diff"],
        #         "head_to_head_game_win": head_to_head_diff["team_b_base"]["head_to_head_game_win"],
        #         "head_to_head_game_loss": head_to_head_diff["team_b_base"]["head_to_head_game_loss"],
        #         "head_to_head_series_win": head_to_head_diff["team_b_base"]["head_to_head_series_win"],
        #         "head_to_head_series_loss": head_to_head_diff["team_b_base"]["head_to_head_series_loss"],
        #         "latest_game_win_diff": latest_match_diff["team_b_base"]["latest_game_win_diff"],
        #         "latest_game_loss_diff": latest_match_diff["team_b_base"]["latest_game_loss_diff"],
        #         "latest_series_win_diff": latest_match_diff["team_b_base"]["latest_series_win_diff"],
        #         "latest_series_loss_diff": latest_match_diff["team_b_base"]["latest_series_loss_diff"],
        #         "playoff_h2h_win": 0,
        #         "playoff_h2h_loss": 0,
        #         "playoff_upper_bracket_win_diff": 0,
        #         "playoff_lower_bracket_win_diff": 0,
        #         "is_grand_final":0,
        #         "win": matchup["is_team_b_win"]
        #     }
        # }

        result = {
             "team_a_base" : {
                "overall_rank_diff": overall_team_diff["team_a_base"]["rank_diff"],
                "overall_game_win_rate_diff": overall_team_diff["team_a_base"]["game_win_rate_diff"],
                "overall_series_win_rate_diff": overall_team_diff["team_a_base"]["series_win_rate_diff"],
                "head_to_head_game_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_game_win_rate_diff"],
                "head_to_head_series_win_rate_diff": head_to_head_diff["team_a_base"]["head_to_head_series_win_rate_diff"],
                "latest_series_win_rate_diff": latest_match_diff["team_a_base"]["latest_series_win_rate_percentage_diff"],
                "latest_game_win_rate_diff": latest_match_diff["team_a_base"]["latest_game_win_rate_percentage_diff"],
                "win": matchup["is_team_a_win"]
             },
             "team_b_base" : {
                "overall_rank_diff": overall_team_diff["team_b_base"]["rank_diff"],
                "overall_game_win_rate_diff": overall_team_diff["team_b_base"]["game_win_rate_diff"],
                "overall_series_win_rate_diff": overall_team_diff["team_b_base"]["series_win_rate_diff"],
                "head_to_head_game_win_rate_diff": head_to_head_diff["team_b_base"]["head_to_head_game_win_rate_diff"],
                "head_to_head_series_win_rate_diff": head_to_head_diff["team_b_base"]["head_to_head_series_win_rate_diff"],
                "latest_series_win_rate_diff": latest_match_diff["team_b_base"]["latest_series_win_rate_percentage_diff"],
                "latest_game_win_rate_diff": latest_match_diff["team_b_base"]["latest_game_win_rate_percentage_diff"],
                "win": matchup["is_team_b_win"]
             }
        }


        pprint(result)
        csv([result["team_a_base"], result["team_b_base"]], "ml_dataset.csv")

get_matchups(matchups, standings, matches)



# overall_team_diff = get_team_diff(
#     standings,
#     "GEEK",
#     "EVOS"
# )

# head_to_head_diff = get_head_to_head_diff(
#     matches,
#     "GEEK",
#     "EVOS"
# )

# latest_match_diff = get_latest_match_diff(
#     matches,
#     "GEEK",
#     "EVOS"
# )
# pprint([overall_team_diff, head_to_head_diff, latest_match_diff])

