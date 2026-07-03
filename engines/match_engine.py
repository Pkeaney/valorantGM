import random
from models.player import Player

##Function involves
## For loop to loop over all maps which are listed as active in the database
def generate_map_pool(maps):

    return [m for m in maps if m.active]

##Function involves
##Running generate_map_pool to get all the available maps
##First we confirm bans
##Then we confirm picks
##Then take the first map in remaining pool as the decider (typically we'll have 7 active maps)
##Output it in json format (for now)
def pick_ban_system(team_a, team_b, maps):

    available_maps = generate_map_pool(maps)

    bans = []

    # 1 ban each
    ban_a = random.choice(available_maps)
    available_maps.remove(ban_a)

    ban_b = random.choice(available_maps)
    available_maps.remove(ban_b)

    bans.append(ban_a.map_name)
    bans.append(ban_b.map_name)

    # picks (each team picks 1 map)
    pick_a = random.choice(available_maps)
    available_maps.remove(pick_a)

    pick_b = random.choice(available_maps)
    available_maps.remove(pick_b)

    # decider = last map
    decider = available_maps[0] if available_maps else None

    final_map_pool = [pick_a, pick_b, decider]

    return final_map_pool, {
        "bans": bans,
        "picks": [pick_a.map_name, pick_b.map_name],
        "decider": decider.map_name if decider else None
    }


## Function involves
## - define wins to 0 for both teams
## - while loop runs until 2 match wins for either team
## - Run simulate_map function which will simulate the specific match for a result
## - Depending on result of that match, add 1 to team_a or b
def simulate_bo3(team_a, team_b, maps):

    wins_a = 0
    wins_b = 0

    map_results = []

    selected_maps, draft_info = pick_ban_system(team_a, team_b, maps)

    for map_obj in selected_maps:

        strength_a = calculate_team_strength(team_a)
        strength_b = calculate_team_strength(team_b)


        winner = simulate_map(strength_a,strength_b,map_obj)

        map_results.append({
            "map": map_obj.map_name,
            "winner": winner
        })

        if winner == "A":
            wins_a += 1
        else:
            wins_b += 1

    # We want to stop early if one team reaches 2 wins
        if wins_a == 2 or wins_b == 2:
            break
    
    return wins_a, wins_b, map_results, draft_info
    
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
def simulate_map(strength_a, strength_b, map_obj):
    
    diff = strength_a - strength_b

    #map influence (simple for now)
    diff += (map_obj.attack_bias - 0.5) * 10

    probability = 0.5 + diff / 200
    probability = max(0.1, min(0.9, probability))

    return "A" if random.random() < probability else "B"