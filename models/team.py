##base model for the team data to be seeded

from extensions import db

class Team(db.Model):

    __tablename__ = "teams"

    team_id = db.Column(db.Integer, primary_key=True)

    team_name = db.Column(db.String, nullable=False)

    strength = db.Column(db.Integer, default=50)
