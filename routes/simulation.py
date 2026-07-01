##Involves running the simulation_match function from match_engine and displaying it in user friendly format on webpage

from flask import Blueprint, jsonify

from models.team import Team
from models.match import Match
from extensions import db

from engines.match_engine import simulate_match


sim_bp = Blueprint("simulation", __name__)


@sim_bp.route("/simulate-match", methods=["GET","POST"])
def simulate_match_route():


#Get teams from database

    team_a = Team.query.get(1)
    team_b = Team.query.get(2)

    if not team_a or not team_b:
        return jsonify({"error": "Teams not found"}), 404

#Run simulation (simulate_match originates in engines/match_engine.py)

    result = simulate_match(team_a.strength, team_b.strength)

    winner_id = team_a.team_id if result == "A" else team_b.team_id

#Save match details down to database

    match = Match(
        team_a=team_a.team_id,
        team_b=team_b.team_id,
        winner=winner_id
    )

    db.session.add(match)
    db.session.commit()


#Return result to client on webpage in JSON format

    return jsonify({
        "team_a": team_a.team_name,
        "team_b": team_b.team_name,
        "winner": team_a.team_name if result == "A" else team_b.team_name
    })
