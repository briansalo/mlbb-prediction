from collections import defaultdict

def get_latest_match_diff(matches, team_a, team_b):
    a = get_latest_matches_record(matches, team_a)
    b = get_latest_matches_record(matches, team_b)

    team_a_base = {
        "team_a": team_a,
        "team_b": team_b,

        "latest_game_win_diff":
            a["game_win"] - b["game_win"],

        "latest_game_loss_diff":
            a["game_loss"] - b["game_loss"],

        "latest_series_win_diff":
            a["series_win"] - b["series_win"],

        "latest_series_loss_diff":
            a["series_loss"] - b["series_loss"],

        "latest_game_win_rate_percentage_diff":
            a["win_match_rate_percentage"] -
            b["win_match_rate_percentage"],

        "latest_series_win_rate_percentage_diff":
            a["win_series_rate_percentage"] -
            b["win_series_rate_percentage"],
    }

    team_b_base = {
        "team_a": team_b,
        "team_b": team_a,

        "latest_game_win_diff":
            -team_a_base["latest_game_win_diff"],

        "latest_game_loss_diff":
            -team_a_base["latest_game_loss_diff"],

        "latest_series_win_diff":
            -team_a_base["latest_series_win_diff"],

        "latest_series_loss_diff":
            -team_a_base["latest_series_loss_diff"],

        "latest_game_win_rate_percentage_diff":
            -team_a_base["latest_game_win_rate_percentage_diff"],

        "latest_series_win_rate_percentage_diff":
            -team_a_base["latest_series_win_rate_percentage_diff"],
    }

    return {
        "team_a_base": team_a_base,
        "team_b_base": team_b_base
    }
    
def get_latest_matches_record(matches, team_ticker, limit=7):
    team_matches = []

    for match in matches:
        if (
            match["team_a_ticker"] == team_ticker or
            match["team_b_ticker"] == team_ticker
        ):
            team_matches.append(match)

    # latest first
    team_matches.sort(
        key=lambda x: x["match_id"],
        reverse=True
    )

    latest_matches = team_matches[:limit]

    result = {
        "ticker": team_ticker,
        "matches_played": len(latest_matches),
        "series_win": 0,
        "series_loss": 0,
        "game_win": 0,
        "game_loss": 0,
        "win_series_rate_percentage": 0,
        "win_match_rate_percentage": 0,
    }

    for match in latest_matches:

        if match["team_a_ticker"] == team_ticker:
            game_win = match["score_a"]
            game_loss = match["score_b"]
            winner_side = "a"
        else:
            game_win = match["score_b"]
            game_loss = match["score_a"]
            winner_side = "b"

        result["game_win"] += game_win
        result["game_loss"] += game_loss

        if match["winner_team"] == winner_side:
            result["series_win"] += 1
        else:
            result["series_loss"] += 1

    total_series = (
        result["series_win"] +
        result["series_loss"]
    )

    total_games = (
        result["game_win"] +
        result["game_loss"]
    )

    if total_series > 0:
        result["win_series_rate_percentage"] = round(
            result["series_win"] / total_series * 100,
            2
        )

    if total_games > 0:
        result["win_match_rate_percentage"] = round(
            result["game_win"] / total_games * 100,
            2
        )

    return result

def get_team_record(matches, ticker):
    standings = get_team_records(matches)

    for team in standings:
        if team["ticker"] == ticker:
            return team

    return None

def get_head_to_head_diff(matches, team_a_ticker, team_b_ticker):
    team_a_base = {
        "team_a": team_a_ticker,
        "team_b": team_b_ticker,

        "head_to_head_game_win": 0,
        "head_to_head_game_loss": 0,
        "head_to_head_game_win_diff": 0,
        "head_to_head_game_loss_diff": 0,

        "head_to_head_series_win": 0,
        "head_to_head_series_loss": 0,
        "head_to_head_series_win_diff": 0,
        "head_to_head_series_loss_diff": 0,

        "matches_found": 0,
        "series": []
    }

    for match in matches:
        ticker_a = match["team_a_ticker"]
        ticker_b = match["team_b_ticker"]

        is_match = (
            (ticker_a == team_a_ticker and ticker_b == team_b_ticker) or
            (ticker_a == team_b_ticker and ticker_b == team_a_ticker)
        )

        if not is_match:
            continue

        team_a_base["matches_found"] += 1

        score_a = match["score_a"]
        score_b = match["score_b"]

        if ticker_a == team_a_ticker:
            selected_score = score_a
            opponent_score = score_b
            selected_winner_team = "a"
        else:
            selected_score = score_b
            opponent_score = score_a
            selected_winner_team = "b"

        team_a_base["head_to_head_game_win"] += selected_score
        team_a_base["head_to_head_game_loss"] += opponent_score

        if match["winner_team"] == selected_winner_team:
            team_a_base["head_to_head_series_win"] += 1
        else:
            team_a_base["head_to_head_series_loss"] += 1

        team_a_base["series"].append([selected_score, opponent_score])

    team_a_base["head_to_head_game_win_diff"] = (
        team_a_base["head_to_head_game_win"] -
        team_a_base["head_to_head_game_loss"]
    )

    team_a_base["head_to_head_game_loss_diff"] = (
        team_a_base["head_to_head_game_loss"] -
        team_a_base["head_to_head_game_win"]
    )

    team_a_base["head_to_head_series_win_diff"] = (
        team_a_base["head_to_head_series_win"] -
        team_a_base["head_to_head_series_loss"]
    )

    team_a_base["head_to_head_series_loss_diff"] = (
        team_a_base["head_to_head_series_loss"] -
        team_a_base["head_to_head_series_win"]
    )

    team_b_base = {
        "team_a": team_b_ticker,
        "team_b": team_a_ticker,

        "head_to_head_game_win": team_a_base["head_to_head_game_loss"],
        "head_to_head_game_loss": team_a_base["head_to_head_game_win"],

        "head_to_head_game_win_diff": -team_a_base["head_to_head_game_win_diff"],
        "head_to_head_game_loss_diff": -team_a_base["head_to_head_game_loss_diff"],

        "head_to_head_series_win": team_a_base["head_to_head_series_loss"],
        "head_to_head_series_loss": team_a_base["head_to_head_series_win"],

        "head_to_head_series_win_diff": -team_a_base["head_to_head_series_win_diff"],
        "head_to_head_series_loss_diff": -team_a_base["head_to_head_series_loss_diff"],

        "matches_found": team_a_base["matches_found"],
        "series": [
            [score_b, score_a]
            for score_a, score_b in team_a_base["series"]
        ]
    }

    return {
        "team_a_base": team_a_base,
        "team_b_base": team_b_base
    }
    
def get_team_diff(standings, team_a_ticker, team_b_ticker):
    team_a = None
    team_b = None

    for team in standings:
        if team["ticker"] == team_a_ticker:
            team_a = team

        if team["ticker"] == team_b_ticker:
            team_b = team

    if team_a is None:
        raise ValueError(f"Team not found: {team_a_ticker}")

    if team_b is None:
        raise ValueError(f"Team not found: {team_b_ticker}")

    team_a_base = {
        "team_a": team_a_ticker,
        "team_b": team_b_ticker,

        "game_win_diff":
            team_a["game_win"] - team_b["game_win"],

        "game_loss_diff":
            team_a["game_loss"] - team_b["game_loss"],

        "series_win_diff":
            team_a["series_win"] - team_b["series_win"],

        "series_loss_diff":
            team_a["series_loss"] - team_b["series_loss"],

        "rank_diff":
            team_a["rank"] - team_b["rank"]
    }

    team_b_base = {
        "team_a": team_b_ticker,
        "team_b": team_a_ticker,

        "game_win_diff":
            team_b["game_win"] - team_a["game_win"],

        "game_loss_diff":
            team_b["game_loss"] - team_a["game_loss"],

        "series_win_diff":
            team_b["series_win"] - team_a["series_win"],

        "series_loss_diff":
            team_b["series_loss"] - team_a["series_loss"],

        "rank_diff":
            team_b["rank"] - team_a["rank"]
    }

    return {
        "team_a_base": team_a_base,
        "team_b_base": team_b_base
    }
def get_team_records(matches):
    records = defaultdict(lambda: {
        "team": "",
        "ticker": "",
        "matches_played": 0,
        "series_win": 0,
        "series_loss": 0,
        "game_win": 0,
        "game_loss": 0,
        "game_diff": 0,
        "points": 0,
    })

    for match in matches:
        ticker_a = match["team_a_ticker"]
        ticker_b = match["team_b_ticker"]

        team_a = match["team_a"]
        team_b = match["team_b"]

        score_a = match["score_a"]
        score_b = match["score_b"]

        # Initialize
        records[ticker_a]["team"] = team_a
        records[ticker_a]["ticker"] = ticker_a

        records[ticker_b]["team"] = team_b
        records[ticker_b]["ticker"] = ticker_b

        # Matches played
        records[ticker_a]["matches_played"] += 1
        records[ticker_b]["matches_played"] += 1

        # Game wins/losses
        records[ticker_a]["game_win"] += score_a
        records[ticker_a]["game_loss"] += score_b

        records[ticker_b]["game_win"] += score_b
        records[ticker_b]["game_loss"] += score_a

        # Series wins/losses
        if match["winner_team"] == "a":
            records[ticker_a]["series_win"] += 1
            records[ticker_b]["series_loss"] += 1

        elif match["winner_team"] == "b":
            records[ticker_b]["series_win"] += 1
            records[ticker_a]["series_loss"] += 1

    # Final calculations
    standings = []

    for team in records.values():
        team["points"] = team["series_win"]
        team["game_diff"] = team["game_win"] - team["game_loss"]

        standings.append(team)

    standings.sort(
        key=lambda x: (
            -x["points"],
            -x["game_diff"],
            -x["game_win"]
        )
    )

    for rank, team in enumerate(standings, start=1):
        team["rank"] = rank

    return standings