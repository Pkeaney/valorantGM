##base model for the match data to be seeded

from extensions import db

class Match(db.Model):

    __tablename__ = "matches"

    match_id = db.Column(
        db.Integer,
        primary_key=True
    )

    team_a = db.Column(
        db.Integer
    )

    team_b = db.Column(
        db.Integer
    )

    winner = db.Column(
        db.Integer
    )