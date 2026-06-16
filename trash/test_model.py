import pandas as pd
from xgboost import XGBClassifier

# simple dataset (MLBB style)
# data = {
#     "gold_diff": [5000, -2000, 3000, -1000],
#     "kills_diff": [8, -3, 5, -2],
#     "turtle": [1, 0, 1, 0],
#     "lord": [1, 0, 1, 0],
#     "win": [1, 0, 1, 0]
# }
# [2-0]onic|1
# [1-2]onic|0

# omg vs twis  | onesided
# 1         2   |  0 | 2
# 2         0    | 1 | 

# onic vs aurora  | onesided
# 2         0   |  2 | 0
# 2         1    | 1 | 0

# tlph vs omg | onesided
# 2        0     1 | 0
# 2        0     2
regular_season_standings = [
    {
        "rank": 1,
        "team": "Team Liquid PH",
        "match": "13-1",
        "game": "27-6",
        "diff": "+21",
        "pts": "13p"
    },
    {
        "rank": 2,
        "team": "Team Falcons PH",
        "match": "12-2",
        "game": "26-8",
        "diff": "+18",
        "pts": "12p"
    },
    {
        "rank": 3,
        "team": "ONIC Philippines",
        "match": "9-5",
        "game": "20-13",
        "diff": "+7",
        "pts": "9p"
    },
    {
        "rank": 4,
        "team": "Omega Esports",
        "match": "6-8",
        "game": "15-19",
        "diff": "-4",
        "pts": "6p"
    },
    {
        "rank": 5,
        "team": "Twisted Minds PH",
        "match": "6-8",
        "game": "13-20",
        "diff": "-7",
        "pts": "6p"
    },
    {
        "rank": 6,
        "team": "Aurora Gaming PH",
        "match": "5-9",
        "game": "15-20",
        "diff": "-5",
        "pts": "5p"
    },
    {
        "rank": 7,
        "team": "AP.Bren",
        "match": "3-11",
        "game": "10-24",
        "diff": "-14",
        "pts": "3p"
    },
    {
        "rank": 8,
        "team": "TNC Pro Team",
        "match": "2-12",
        "game": "8-24",
        "diff": "-16",
        "pts": "2p"
    }
]

rank_3_data = regular_season_standings[2]
rank_6_data = regular_season_standings[5]

rank_3_match = list(map(int, rank_3_data['match'].split('-')))
rank_6_match = list(map(int, rank_6_data['match'].split('-')))
rank_3_game = list(map(int, rank_3_data['game'].split('-')))
rank_6_game = list(map(int, rank_6_data['game'].split('-')))

overall_match_win_diff = rank_3_match[0] - rank_6_match[0]
overall_match_loss_diff = rank_3_match[1] - rank_6_match[1]
overall_game_won_diff = rank_3_game[0] - rank_6_game[0]
overall_game_loss_diff = rank_3_game[1] - rank_6_game[1]

# head_to_head_score_diff = 
# print(rank_3_data['rank'])
# print(rank_6_data)
# print(overall_match_win_diff)
# print(overall_match_loss_diff)
# print(overall_game_won_diff)
# print(overall_game_loss_diff)


# print(head_to_head_data[rank_3_data['rank']])
rank_3_matches = head_to_head_data[rank_3_data['rank']]
rank_3_vs_rank_6 = next(match for match in rank_3_matches if match["opponent_rank"] == rank_6_data['rank'])

rank_3_vs_rank_6_win = rank_3_vs_rank_6['score'][0]
rank_3_vs_rank_6_loss = rank_3_vs_rank_6['score'][1]
print(rank_3_vs_rank_6_win)
print(rank_3_vs_rank_6_loss)

# rank_3vs_rank_8 = next(match for match in rank_3_data['matches'] if match["opponent_rank"] == rank_8_data['rank'])
# print(rank_3vs_rank_8)
overall_match_win_diff = rank_3_match[0] - rank_6_match[0]
overall_match_loss_diff = rank_3_match[1] - rank_6_match[1]
overall_game_won_diff = rank_3_game[0] - rank_6_game[0]
overall_game_loss_diff = rank_3_game[1] - rank_6_game[1]

data = {
    "overall_match_win_diff": [4, -4, 0, 0, 7, -7],
    "overall_match_loss_diff": [5, -5, 2, -2, 12, -12],
    "overall_game_won_diff":[2, -2, 0, 0, 2, -2],
    "overall_game_loss_diff":[3, -3, 1, -1, 4, -4],
    "head_to_head_win_diff":[3, -3, 1, -1, 3, -3],
    "head_to_head_loss_diff":[3, -3, 1, -1, 3, -3],
    "win":[1, 0, 1, 0, 1, 0]
}
# data = {
#     "overall_match_point_diff": [4, -4, 0, 0, 7, -7],
#     "overall_match_win_diff": [5, -5, 2, -2, 12, -12],
#     "head_to_head_match_point_diff":[2, -2, 0, 0, 2, -2],
#     "head_to_head_match_win_diff":[3, -3, 1, -1, 4, -4],
#     "head_to_head_one_sided_diff":[3, -3, 1, -1, 3, -3],
#     "win":[1, 0, 1, 0, 1, 0]
# }


df = pd.DataFrame(data)

X = df.drop("win", axis=1)
y = df["win"]

model = XGBClassifier()
model.fit(X, y)

# test prediction (new match)
# new_match = [[4000, 6, 1, 1]]

# onic vs falcon | onesided
# 1        2        0 | 2
# 1        2        0  | 2

new_match = [[-3, -6, -2, -2, -4]]
prediction = model.predict(new_match)
proba = model.predict_proba(new_match)

print("Lose probability:", proba[0][0])
print("Win probability:", proba[0][1])
print("Prediction (1=Win, 0=Lose):", prediction[0])