##base model for the player data to be seeded

from extensions import db

class Player(db.Model):

    __tablename__ = "players"

    player_id = db.Column(db.Integer, primary_key=True)

    ign = db.Column(db.String, nullable=False)

    current_team_id = db.Column(db.Integer)

    current_ability = db.Column(db.Integer, default=50)
