import joblib
from pprint import pprint
from services.predict import predict_matchup
from services.matches import get_team_records
from data.matches.id.id_season_17_matches import matches
from data.matchups.id.season_17 import matchups

standings = get_team_records(matches)

for matchup in matchups:
    team_a = matchup["team_a"]
    team_b = matchup["team_b"]
    model_name = "models/id/face_off_14.pkl"
    model = joblib.load(model_name)
    result = predict_matchup(model_name, standings, matches, team_a, team_b)

    pprint(result)
    new_match = [result]

    prediction = model.predict(new_match)
    probability = model.predict_proba(new_match)

    print(f"----Prediction for {team_a} vs {team_b} -----")
    print(f"Win Probability: {probability[0][1] * 100:.2f}%")
    print(f"Lose Probability: {probability[0][0] * 100:.2f}%")
    print(f"---------------")