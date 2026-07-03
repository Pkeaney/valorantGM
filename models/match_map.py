from extensions import db


class MatchMap(db.Model):

    __tablename__ = "match_maps"

    id = db.Column(db.Integer, primary_key=True)

    match_id = db.Column(
        db.Integer,
        db.ForeignKey("matches.match_id")
    )

    map_id = db.Column(
        db.Integer,
        db.ForeignKey("maps.map_id")
    )

    winner_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.team_id")
    )

    loser_id = db.Column(
        db.Integer,
        db.ForeignKey("teams.team_id")
    )

    map_order = db.Column(db.Integer)