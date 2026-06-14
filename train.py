import pandas as pd
from data.season8 import regular_season_standings
from data.season8 import head_to_head_data
from data.season8 import latest_games_win_rate


CSV_FILE = "ml_dataset.csv"
# -----------------------------
# HELPERS
# -----------------------------
def get_team_by_rank(rank):
    return next(t for t in regular_season_standings if t["rank"] == rank)


def get_head_to_head(rank_a, rank_b):
    matches = head_to_head_data.get(rank_a, [])
    return next((m for m in matches if m["opponent_rank"] == rank_b), None)


def get_latest_win_rate_by_rank(rank):
    return next(t for t in latest_games_win_rate if t["rank_id"] == rank)


def parse(x):
    return list(map(int, x.split("-")))


def _get_match_wins_losses(team):
    if "match_wins" in team and "match_losses" in team:
        return team["match_wins"], team["match_losses"]
    if "match" in team:
        return parse(team["match"])
    return 0, 0


def _get_game_wins_losses(team):
    if "game_wins" in team and "game_losses" in team:
        return team["game_wins"], team["game_losses"]
    if "game" in team:
        return parse(team["game"])
    return 0, 0


def _pick_latest_rate(latest_entry):
    for key in ("win_match_rate_percentage", "win_series_rate_percentage", "win_rate_percentage"):
        if key in latest_entry:
            return latest_entry[key]
    return 0.0


def _pick_latest_match_rate(latest_entry):
    for key in ("win_match_rate_percentage", "win_rate_percentage"):
        if key in latest_entry:
            return latest_entry[key]
    return 0.0


def _pick_latest_series_rate(latest_entry):
    for key in ("win_series_rate_percentage", "win_rate_percentage"):
        if key in latest_entry:
            return latest_entry[key]
    return 0.0


def _get_head_to_head_stats(h2h):
    if not h2h:
        return 0, 0, 0, 0
    if "win" in h2h and "loss" in h2h:
        series_win = h2h.get("series_win", 0)
        series_loss = h2h.get("series_loss", 0)
        return h2h["win"], h2h["loss"], series_win, series_loss
    if "score" in h2h:
        win = h2h["score"][0]
        loss = h2h["score"][1]
        series_win = h2h.get("series_win", 0)
        series_loss = h2h.get("series_loss", 0)
        return win, loss, series_win, series_loss
    return 0, 0, 0, 0


def _invert_diff(value):
    return 0 - value


# -----------------------------
# FEATURE ENGINE
# -----------------------------
def compute_features(rank_a, rank_b):
    a = get_team_by_rank(rank_a)
    b = get_team_by_rank(rank_b)

    a_mw, a_ml = _get_match_wins_losses(a)
    b_mw, b_ml = _get_match_wins_losses(b)

    a_gw, a_gl = _get_game_wins_losses(a)
    b_gw, b_gl = _get_game_wins_losses(b)

    # rank difference based on input ranks (A - B)
    rank_diff = rank_a - rank_b

    features = {
        "rank_diff": rank_diff,
        "overall_match_win_diff": a_mw - b_mw,
        "overall_match_loss_diff": a_ml - b_ml,
        "overall_game_won_diff": a_gw - b_gw,
        "overall_game_loss_diff": a_gl - b_gl,
    }

    latest_a = get_latest_win_rate_by_rank(rank_a)
    latest_b = get_latest_win_rate_by_rank(rank_b)
    features["latest_game_win_match_rate_percentage_diff"] = (
        _pick_latest_match_rate(latest_a) - _pick_latest_match_rate(latest_b)
    )
    features["latest_game_win_series_rate_percentage_diff"] = (
        _pick_latest_series_rate(latest_a) - _pick_latest_series_rate(latest_b)
    )

    h2h = get_head_to_head(rank_a, rank_b)
    win, loss, series_win, series_loss = _get_head_to_head_stats(h2h)
    features["head_to_head_win"] = win
    features["head_to_head_loss"] = loss
    features["head_to_head_win_series"] = series_win
    features["head_to_head_loss_series"] = series_loss

    return features


# -----------------------------
# MIRROR FEATURE GENERATOR
# -----------------------------
def mirror_features(f):
    return {
        "rank_diff": _invert_diff(f["rank_diff"]),
        "overall_match_win_diff": _invert_diff(f["overall_match_win_diff"]),
        "overall_match_loss_diff": _invert_diff(f["overall_match_loss_diff"]),
        "overall_game_won_diff": _invert_diff(f["overall_game_won_diff"]),
        "overall_game_loss_diff": _invert_diff(f["overall_game_loss_diff"]),
        "head_to_head_win": f["head_to_head_loss"],
        "head_to_head_loss": f["head_to_head_win"],
        "head_to_head_win_series": f["head_to_head_loss_series"],
        "head_to_head_loss_series": f["head_to_head_win_series"],
        "latest_game_win_match_rate_percentage_diff": _invert_diff(f["latest_game_win_match_rate_percentage_diff"]),
        "latest_game_win_series_rate_percentage_diff": _invert_diff(f["latest_game_win_series_rate_percentage_diff"]),
    }


# -----------------------------
# BUILD ROW
# -----------------------------
def build_row(features, label):
    return {
        "rank_diff": features["rank_diff"],
        "overall_match_win_diff": features["overall_match_win_diff"],
        "overall_match_loss_diff": features["overall_match_loss_diff"],
        "overall_game_won_diff": features["overall_game_won_diff"],
        "overall_game_loss_diff": features["overall_game_loss_diff"],
        "head_to_head_win": features["head_to_head_win"],
        "head_to_head_loss": features["head_to_head_loss"],
        "head_to_head_win_series": features["head_to_head_win_series"],
        "head_to_head_loss_series": features["head_to_head_loss_series"],
        "latest_game_win_match_rate_percentage_diff": features["latest_game_win_match_rate_percentage_diff"],
        "latest_game_win_series_rate_percentage_diff": features["latest_game_win_series_rate_percentage_diff"],
        "win": label
    }


# -----------------------------
# SAVE CSV
# -----------------------------
def save(rows):
    df = pd.DataFrame(rows)

    try:
        old = pd.read_csv(CSV_FILE)
        df = pd.concat([old, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv(CSV_FILE, index=False)


# -----------------------------
# MAIN INPUT FLOW
# -----------------------------
def prompt():
    print("\n=== ML DATA BUILDER (AUTO MIRROR MODE) ===")

    a_input = input("Rank A (or exit): ").strip().lower()
    if a_input == "exit":
        return False

    b_input = input("Rank B (or exit): ").strip().lower()
    if b_input == "exit":
        return False

    try:
        a = int(a_input)
        b = int(b_input)
    except ValueError:
        print("Invalid rank. Please enter numeric rank values or 'exit'.")
        return True

    try:
        team_a = get_team_by_rank(a)["team"]
    except StopIteration:
        print("Rank A not found. Please check the rank or enter 'exit'.")
        return True

    try:
        team_b = get_team_by_rank(b)["team"]
    except StopIteration:
        print("Rank B not found. Please check the rank or enter 'exit'.")
        return True

    print(f"\nDid {team_a} win over {team_b}?")
    print("1 = Win")
    print("0 = Loss")
    print("exit = Cancel")
    label_input = input("Label: ").strip().lower()
    if label_input == "exit":
        print("Canceled. Returning to main menu.")
        return True

    if label_input not in ("0", "1"):
        print("Invalid label. Enter 1, 0, or exit.")
        return True

    label = int(label_input)

    # -----------------------------
    # original direction (A vs B)
    # -----------------------------
    f_ab = compute_features(a, b)
    print(f_ab)
    row_ab = build_row(f_ab, label)

    # -----------------------------
    # mirrored direction (B vs A)
    # -----------------------------
    f_ba = mirror_features(f_ab)
    row_ba = build_row(f_ba, 1 - label)

    save([row_ab, row_ba])

    print("\n✅ Saved BOTH directions:")
    print("A vs B:", row_ab)
    print("B vs A:", row_ba)


# -----------------------------
# RUN LOOP
# -----------------------------
if __name__ == "__main__":
    while True:
        keep_running = prompt()
        if not keep_running:
            break

        again = input("\nAdd another match? (y/n): ").strip().lower()
        if again != "y":
            break
