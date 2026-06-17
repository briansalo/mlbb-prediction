
from services.matches import get_playoff_records, get_team_records, get_team_diff, get_head_to_head_diff, get_latest_matches_record, get_latest_match_diff
from services.input import prompt_compare
from services.playoffs_matches import get_playoff_dataset
from services.season_matches import get_season_dataset

from services.export import csv
from pprint import pprint
from collections import defaultdict
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
    (season_5_matchups, season_5_matches),
    (season_6_matchups, season_6_matches),
    (season_7_matchups, season_7_matches),
    (season_8_matchups, season_8_matches),
    (season_9_matchups, season_9_matches),
    (season_10_matchups, season_10_matches),
    (season_11_matchups, season_11_matches),
    (season_12_matchups, season_12_matches),
    (season_13_matchups, season_13_matches),
    (season_14_matchups, season_14_matches)
]





for index, (matchups, matches) in enumerate(seasons, start=1):
    standings = get_team_records(matches) 
    get_season_dataset(matchups, standings, matches, "datasets/id/season_14.csv")
    print(f" Season #{index}")


for index, (matchups, matches) in enumerate(seasons, start=1):
    standings = get_team_records(matches)

    # Season + upper quarter → predict upper semi final
    get_playoff_dataset(
        matchups,
        standings,
        matches,
        preload_stages=[
            "is_upper_quarter_final"
        ],
        target_stage="is_upper_semi_final",
        dataset_name="datasets/id/upper_semi_final_14.csv"
    )

    # Season + upper quarter + upper semi → predict lower semi final
    get_playoff_dataset(
        matchups,
        standings,
        matches,
        preload_stages=[
            "is_upper_quarter_final",
            "is_upper_semi_final"
        ],
        target_stage="is_lower_semi_final",
        dataset_name="datasets/id/lower_semi_final_14.csv"
    )

    # # Season + upper quarter + upper semi + lower semi → predict upper final
    get_playoff_dataset(
        matchups,
        standings,
        matches,
        preload_stages=[
            "is_upper_quarter_final",
            "is_upper_semi_final",
            "is_lower_semi_final"
        ],
        target_stage="is_upper_final",
        dataset_name="datasets/id/upper_final_14.csv"
    )

    # # Season + upper quarter + upper semi + lower semi + upper final → predict lower final
    get_playoff_dataset(
        matchups,
        standings,
        matches,
        preload_stages=[
            "is_upper_quarter_final",
            "is_upper_semi_final",
            "is_lower_semi_final",
            "is_upper_final"
        ],
        target_stage="is_lower_final",
        dataset_name="datasets/id/lower_final_14.csv"
    )

    # # Everything before grand final → predict grand final
    get_playoff_dataset(
        matchups,
        standings,
        matches,
        preload_stages=[
            "is_upper_quarter_final",
            "is_upper_semi_final",
            "is_lower_semi_final",
            "is_upper_final",
            "is_lower_final"
        ],
        target_stage="is_grand_final",
        dataset_name="datasets/id/grand_final_14.csv"
    )

    print(f"Season #{index}")
