import joblib
from services.matches import get_team_records, get_team_diff, get_head_to_head_diff, get_latest_matches_record, get_latest_match_diff
from data.matches.id.id_season_13_matches import matches
from pprint import pprint

def get_matchups(model):
    currentModel = joblib.load(model)
    standings = get_team_records(matches)
    overall_team_diff = get_team_diff(
        standings,
        "ONIC",
        "EVOS"
    )

    head_to_head_diff = get_head_to_head_diff(
        matches,
        "ONIC",
        "EVOS"
    )
    latest_match_diff = get_latest_match_diff(
        matches,
        "ONIC",
        "EVOS"
    )
    result = [
        overall_team_diff["team_a_base"]["rank_diff"],
        overall_team_diff["team_a_base"]["series_win_diff"],
        overall_team_diff["team_a_base"]["series_loss_diff"],
        overall_team_diff["team_a_base"]["game_win_diff"],
        overall_team_diff["team_a_base"]["game_loss_diff"],
        head_to_head_diff["team_a_base"]["head_to_head_game_win"],
        head_to_head_diff["team_a_base"]["head_to_head_game_loss"],
        head_to_head_diff["team_a_base"]["head_to_head_series_win"],
        head_to_head_diff["team_a_base"]["head_to_head_series_loss"],
        latest_match_diff["team_a_base"]["latest_game_win_diff"],
        latest_match_diff["team_a_base"]["latest_game_loss_diff"],
        latest_match_diff["team_a_base"]["latest_series_win_diff"],
        latest_match_diff["team_a_base"]["latest_series_loss_diff"],
        0,
        0,
        0,
        0,
        0
    ]