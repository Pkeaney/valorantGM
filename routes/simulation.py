##Involves running the simulation_match function from match_engine and displaying it in user friendly format on webpage

from flask import Blueprint, jsonify
from models.team import Team
from models.match import Match
from extensions import db
from engines.match_engine import (
    simulate_bo3,
    calculate_team_strength
)


sim_bp = Blueprint("simulation", __name__)
@sim_bp.route("/simulate-match", methods=["GET","POST"])

## Function involves
## - Retrieves team_a and team_b from database
## - Runs calculate_team_strength function to generate strength of team_a and team_b
## - Runs simulate_bo3 function to generate results for each game and end with a winning team
## - Verifies which team is the winner based on results of simulate_bo3 function
## - Return results in json format (for now)
def simulate_match_route():

    teams = Team.query.limit(2).all()

    if len(teams) < 2:
        return jsonify({
            "error": "Teams not found"
        })
    
    team_a = Team.query.filter_by(team_name="Fnatic").first()
    team_b = Team.query.filter_by(team_name="Sentinels").first()

    if not team_a or not team_b:
        return jsonify({"error": "Teams not found"}), 404

    strength_a = calculate_team_strength(team_a)
    strength_b = calculate_team_strength(team_b)

    score_a, score_b = simulate_bo3(
        strength_a,
        strength_b
    )

    winner_team = team_a
    if score_b > score_a:
        winner_team = team_b
        
#Save match details down to database
    match = Match(
        team_a=team_a.team_id,
        team_b=team_b.team_id,
        winner=winner_team.team_id
    )

    db.session.add(match)
    db.session.commit()

#Return result to client on webpage in JSON format
    return jsonify({

        "team_a": team_a.team_name,

        "team_b": team_b.team_name,

        "strength_a": round(
            strength_a,
            1
        ),
        "strength_b": round(
            strength_b,
            1
        ),

        "score":
            f"{score_a}-{score_b}",

        "winner":
            winner_team.team_name
    })
