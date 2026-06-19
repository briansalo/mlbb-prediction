from data.matches.id.id_season_15_matches import matches
from data.matchups.id.season_15 import matchups
from pprint import pprint

def get_playoff_match_data(team_1, team_2, match_history):
    # 1. Find the match between these two teams
    target_match = None
    for match in match_history:
        if (match["team_a"] == team_1 and match["team_b"] == team_2) or \
           (match["team_a"] == team_2 and match["team_b"] == team_1):
            target_match = match
            break
            
    # If no such matchup exists at all in the tournament data, return empty
    if not target_match:
        return {}
        
    bracket_stage = target_match["bracket"]
    
    # 2. If it's the opening round (Quarter Finals), no prerequisites are needed
    if bracket_stage == "upper_quarter_final":
        return target_match

    # 3. For later stages, verify if BOTH teams have played their required previous matches
    # We track if each team has a valid history leading up to this bracket stage
    team_1_ready = False
    team_2_ready = False
    
    for match in match_history:
        # We look at matches that happened BEFORE the target bracket stage
        if match["bracket"] != bracket_stage:
            # Check if team_1 played in any earlier match
            if match["team_a"] == team_1 or match["team_b"] == team_1:
                team_1_ready = True
            # Check if team_2 played in any earlier match
            if match["team_a"] == team_2 or match["team_b"] == team_2:
                team_2_ready = True
                
    # Special Case: Seeds like RRQ or BTR who skip Quarter Finals and start at Upper Semis
    # If the target match is Upper Semi Final, teams starting there don't need prior history
    if bracket_stage == "upper_semi_final":
        # RRQ and BTR are seeded directly into upper_semi_final, so they are always ready
        seeded_teams = ["RRQ", "BTR"] 
        if team_1 in seeded_teams: team_1_ready = True
        if team_2 in seeded_teams: team_2_ready = True

    # 4. Return data only if both teams' prerequisites are met
    if team_1_ready and team_2_ready:
        return target_match
    
    return {}

pprint("AE vs ONIC:", get_playoff_match_data("GEEK", "ONIC", matchups))
