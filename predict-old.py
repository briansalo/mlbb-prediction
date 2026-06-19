import joblib
from pprint import pprint
from services.predict import predict_matchup
from services.matches import get_team_records
from services.playoffs_matches import get_playoff_dataset
from data.matches.id.id_season_15_matches import matches
from data.matchups.id.season_15 import matchups
from services.playoff_predict import predict_playoff_matchup
import pandas as pd

def matchup(matchups, modeltest, standings):
    for matchup in matchups:
        team_a = matchup["team_a"]
        team_b = matchup["team_b"]
        model = ""
        pprint(matchup["bracket"])
        match matchup["bracket"]:
            case "upper_quarter_final":
                model = "models/id/face_off_14.pkl"

            case "upper_semi_final":
                model = "models/id/upper_semi_final_14.pkl"
            case "lower_semi_final":
                model = "models/id/lower_semi_final_14.pkl"
            case "upper_final":
                model = "models/id/upper_final_14.pkl"
            case "lower_final":
                model = "models/id/lower_final_14.pkl"
            case "grand_final":
                model = "models/id/grand_final_14.pkl"
        pprint(model)
        current_model = joblib.load(model)
        # result = predict_matchup(matchups, model, standings, matches, team_a, team_b, matchup)
        result = predict_playoff_matchup(matchups, standings, matches, team_a, team_b, matchup["bracket"])
        pprint("---result-----")
        pprint(result)
        new_match = pd.DataFrame([result])

        prediction = current_model.predict(new_match)
        probability = current_model.predict_proba(new_match)

        print(f"----Prediction for {team_a} vs {team_b} -----")
        print(f"Win Probability: {probability[0][1] * 100:.2f}%")
        print(f"Lose Probability: {probability[0][0] * 100:.2f}%")
        print(f"---------------")

standings = get_team_records(matches)

matchup(matchups, "models/id/face_off_14.pkl", standings)
