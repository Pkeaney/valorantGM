from extensions import db

class Standing(db.Model):

    __tablename__ = "standings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    team_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.team_id"),
        unique=True
    )

    team_name = db.Column(
        db.String, 
        nullable=False
    )

    wins = db.Column(
        db.Integer,
        default=0
    )

    losses = db.Column(
        db.Integer,
        default=0
    )

    maps_won = db.Column(
        db.Integer,
        default=0
    )

    maps_lost = db.Column(
        db.Integer,
        default=0
    )