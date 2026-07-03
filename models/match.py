##base model for the match data to be seeded

from extensions import db

class Match(db.Model):

    __tablename__ = "matches"

    match_id = db.Column(
        db.Integer,
        primary_key=True
    )

    team_a_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.team_id")
    )

    team_b_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.team_id")
    )

    winner_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.team_id")
    )

    loser_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.team_id")
    )

    score_a = db.Column(db.Integer)

    score_b = db.Column(db.Integer)

    played_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )