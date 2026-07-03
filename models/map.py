from extensions import db


class Map(db.Model):

    __tablename__ = "maps"

    map_id = db.Column(db.Integer, primary_key=True)

    map_name = db.Column(db.String(50), nullable=False)

    attack_bias = db.Column(db.Float, default=0.5)

    defense_bias = db.Column(db.Float, default=0.5)

    active = db.Column(db.Boolean, default=True)