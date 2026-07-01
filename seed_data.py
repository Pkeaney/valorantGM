##Script used to seed in data, only to be used for testing for now.

from app import create_app
from models.team import Team
from models.player import Player
from extensions import db

print("SEED SCRIPT STARTED")

app = create_app()

def seed_teams():

    print("Seeding teams...")
    
    teams = [
        Team(team_name="Sentinels", strength=79),
        Team(team_name="Fnatic", strength=81),
        Team(team_name="Gen.G", strength=79),
        Team(team_name="Paper Rex", strength=90),
        Team(team_name="DRX", strength=82),
        Team(team_name="LOUD", strength=77),
        Team(team_name="NAVI", strength=75),
        Team(team_name="Heretics", strength=80),
    ]

    db.session.add_all(teams)
    db.session.commit()

    print("Teams seeded")

def seed_players():

    fnatic = Team.query.filter_by(team_name="Fnatic").first()
    sentinels = Team.query.filter_by(team_name="Sentinels").first()
    prx = Team.query.filter_by(team_name="Paper Rex").first()
    geng = Team.query.filter_by(team_name="Gen.G").first()
    
    print(fnatic, sentinels, prx, geng)

    players = [
        # Sentinels
        Player(ign="Zekken", current_team_id=sentinels.team_id, current_ability=89),
        Player(ign="Sacy", current_team_id=sentinels.team_id, current_ability=86),
        Player(ign="TenZ", current_team_id=sentinels.team_id, current_ability=92),
        # Fnatic
        Player(ign="Boaster", current_team_id=fnatic.team_id, current_ability=88),
        Player(ign="Chronicle", current_team_id=fnatic.team_id, current_ability=91),
        Player(ign="Alfajer", current_team_id=fnatic.team_id, current_ability=93),
        # Gen.G
        Player(ign="Meteor", current_team_id=geng.team_id, current_ability=90),
        Player(ign="T3xture", current_team_id=geng.team_id, current_ability=88),
        # Paper Rex
        Player(ign="Jinggg", current_team_id=prx.team_id, current_ability=92),
        Player(ign="F0rsaken", current_team_id=prx.team_id, current_ability=91),
    ]
    
    print(players)

    db.session.add_all(players)
    db.session.commit()

    print("Players seeded")


def seed_all():

    print("Starting full seed...")

    seed_teams()
    seed_players()

    print("Seed complete")

# =====================================
# RUN SCRIPT
# =====================================

if __name__ == "__main__":

    with app.app_context():

        try:
            seed_all()

            # verification (VERY useful)
            print("TEAM COUNT:", Team.query.count())
            print("PLAYER COUNT:", Player.query.count())

        except Exception as e:
            db.session.rollback()
            print("SEED FAILED:")
            print(e)