##Script used to seed in data, only to be used for testing for now.

from app import create_app
from models.team import Team
from models.player import Player
from models.map import Map
from models.standing import Standing
from extensions import db

print("SEED SCRIPT STARTED")

app = create_app()

def seed_teams():

    print("Seeding teams...")
    
    teams = [
        Team(team_name="Sentinels"),
        Team(team_name="Fnatic"),
        Team(team_name="Gen.G"),
        Team(team_name="Paper Rex"),
        Team(team_name="DRX"),
        Team(team_name="LOUD"),
        Team(team_name="NAVI"),
        Team(team_name="Heretics"),
    ]

    db.session.add_all(teams)
    db.session.commit()

    print("Teams seeded")

def seed_players():

    fnatic = Team.query.filter_by(team_name="Fnatic").first()
    sentinels = Team.query.filter_by(team_name="Sentinels").first()
    prx = Team.query.filter_by(team_name="Paper Rex").first()
    drx = Team.query.filter_by(team_name="DRX").first()
    
    print(fnatic, sentinels, prx, drx)

    players = [
        # Sentinels
        Player(ign="johnqt", current_team_id=sentinels.team_id, current_ability=86),
        Player(ign="Reduxx", current_team_id=sentinels.team_id, current_ability=85),
        Player(ign="Jerrwin", current_team_id=sentinels.team_id, current_ability=75),
        Player(ign="JonahP", current_team_id=sentinels.team_id, current_ability=86),
        Player(ign="cortezia", current_team_id=sentinels.team_id, current_ability=84),
        # Fnatic
        Player(ign="Boaster", current_team_id=fnatic.team_id, current_ability=88),
        Player(ign="Kaajak", current_team_id=fnatic.team_id, current_ability=94),
        Player(ign="Alfajer", current_team_id=fnatic.team_id, current_ability=93),
        Player(ign="Crashies", current_team_id=fnatic.team_id, current_ability=87),
        Player(ign="Cloud", current_team_id=fnatic.team_id, current_ability=86),
        # DRX
        Player(ign="Mako", current_team_id=drx.team_id, current_ability=90),
        Player(ign="free1ng", current_team_id=drx.team_id, current_ability=83),
        Player(ign="HYUNMIN", current_team_id=drx.team_id, current_ability=88),
        Player(ign="BeYN", current_team_id=drx.team_id, current_ability=85),
        Player(ign="Yong", current_team_id=drx.team_id, current_ability=80),
        # Paper Rex
        Player(ign="Jinggg", current_team_id=prx.team_id, current_ability=92),
        Player(ign="F0rsaken", current_team_id=prx.team_id, current_ability=94),
        Player(ign="Something", current_team_id=prx.team_id, current_ability=94),
        Player(ign="D4v41", current_team_id=prx.team_id, current_ability=90),
        Player(ign="Invy", current_team_id=prx.team_id, current_ability=86),
    ]
    
    print(players)

    db.session.add_all(players)
    db.session.commit()

    print("Players seeded")


def seed_maps():

    maps = [
        Map(map_name="Ascent", attack_bias=0.50),
        Map(map_name="Bind", attack_bias=0.49),
        Map(map_name="Haven", attack_bias=0.51),
        Map(map_name="Lotus", attack_bias=0.51),
        Map(map_name="Sunset", attack_bias=0.50),
        Map(map_name="Pearl", attack_bias=0.50),
        Map(map_name="Summit", attack_bias=0.53),
    ]

    db.session.add_all(maps)
    db.session.commit()

    print("Maps seeded")

def seed_standings():

    print("Seeding standings")

    teams = Team.query.all()

    print(f"Found {len(teams)} teams")

    for team in teams:
        standing = Standing(
            team_id=team.team_id,
            team_name=team.team_name
        )

        db.session.add(standing)

    db.session.commit()

    print("Standings seeded")

def seed_all():

    print("Starting full seed...")

    seed_teams()
    seed_players()
    seed_maps()
    seed_standings()

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