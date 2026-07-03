##Involves running the simulation_match function from match_engine and displaying it in user friendly format on webpage

from flask import Blueprint, jsonify
from models.team import Team
from models.match import Match
from models.map import Map
from models.match_map import MatchMap
from models.standing import Standing
from extensions import db
from engines.match_engine import simulate_bo3
import random


sim_bp = Blueprint("simulation", __name__)
@sim_bp.route("/simulate-match", methods=["GET","POST"])

## Function involves
## - Retrieves team_a and team_b from database
## - Runs calculate_team_strength function to generate strength of team_a and team_b
## - Runs simulate_bo3 function to generate results for each game and end with a winning team
## - Verifies which team is the winner based on results of simulate_bo3 function
## - Return results in json format (for now)
def simulate_match_route():
    
    team_a = Team.query.order_by(db.func.random()).first()
    team_b = Team.query.filter(Team.team_id != team_a.team_id).order_by(db.func.random()).first()

    
    if not team_a:
        return jsonify({"error": "Team A not found"}), 404

    if not team_b:
        return jsonify({"error": "Team B not found"}), 404

    maps = Map.query.filter_by(active=True).all()

    score_a, score_b, map_results, draft_info = simulate_bo3(
        team_a,
        team_b,
        maps
    )

    winner_team = team_a
    losing_team = team_a
    if score_b > score_a:
        winner_team = team_b
        losing_team = team_a

        
#Match logic
    match = Match(
        team_a_id=team_a.team_id,
        team_b_id=team_b.team_id,
        winner_id=winner_team.team_id,
        loser_id=losing_team.team_id,
        score_a = score_a,
        score_b = score_b
    )

    db.session.add(match)
    db.session.commit()


## Match Map logic
    for index, result in enumerate(map_results):

        map_obj = Map.query.filter_by(
            map_name=result["map"]
        ).first()

        winner_id = team_a.team_id
        loser_id = team_b.team_id

        if result["winner"] == "B":
            winner_id = team_b.team_id
            loser_id = team_a.team_id
        
        mm = MatchMap(
            match_id=match.match_id,
            map_id=map_obj.map_id,
            winner_id=winner_id,
            loser_id=loser_id,
            map_order=index+1
        )

        db.session.add(mm)
    db.session.commit()

## Standing Logic
    winner_standing = Standing.query.filter_by(

        team_id = winner_id
    ).first()

    if winner_standing is None:
        raise Exception(f"Standing not found for team_id: {winner_id}")

    loser_standing = Standing.query.filter_by(

        team_id = loser_id
    ).first()

    if loser_standing is None:
        raise Exception(f"Standing not found for team_id: {loser_id}")

    winner_standing.wins += 1

    loser_standing.losses += 1

    winner_standing.maps_won += max(score_a,score_b)

    winner_standing.maps_lost += min(score_a,score_b)

    loser_standing.maps_won += min(score_a,score_b)

    loser_standing.maps_lost += max(score_a,score_b)

    db.session.commit()

## Return result to client on webpage in JSON format
    return jsonify({

        "team_a": team_a.team_name,

        "team_b": team_b.team_name,

        "score": f"{score_a} - {score_b}",

        "maps": map_results,

        "draft": draft_info,

        "winner": (
            team_a.team_name if score_a > score_b
            else team_b.team_name
        )
    })
