import random
from models.player import Player

## Function involves
## - define wins to 0 for both teams
## - while loop runs until 2 match wins for either team
## - Run simulate_map function which will simulate the specific match for a result
## - Depending on result of that match, add 1 to team_a or b
def simulate_bo3(strength_a, strength_b):

    wins_a = 0
    wins_b = 0

    while wins_a < 2 and wins_b < 2:

        winner = simulate_map(
            strength_a,
            strength_b
        )

        if winner == "A":
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b

## Function involves
## Gets all players from the selected team
## if there are no players registered for the team, for now we default the strength to 50
## Get the sum of all players current_ability
def calculate_team_strength(team):

    players = Player.query.filter_by(
        current_team_id=team.team_id
    ).all()

    if not players:
        return 50

    return sum(
        player.current_ability for player in players
    ) / len(players)


## Function involves
## Get's the difference between strength_a and strength_b
## Conducts formulas to detect the probability of the result
def simulate_map(strength_a, strength_b):
    
    diff = strength_a - strength_b

    probability = 0.5 + diff / 200
    probability = max(0.1, min(0.9, probability))

    if random.random() < probability:
        return "A"
    
    return "B"