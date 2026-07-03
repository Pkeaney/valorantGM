from flask import Blueprint
from flask import jsonify

from models.standing import Standing
from models.team import Team

standings_bp = Blueprint("standings", __name__)
@standings_bp.route("/standings")

def standings():
    standings = Standing.query.order_by(
        Standing.wins.desc()
    ).all()

    results = []

    for standing in standings:
        team = Team.query.get(
            standing.team_id
        )

        results.append({
            "team": team.team_name,
            "wins": standing.wins,
            "losses": standing.losses,
            "maps_won": standing.maps_won,
            "maps_lost": standing.maps_lost,

        })

    return jsonify(
        results
    )