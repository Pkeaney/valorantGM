import random

def simulate_match(team_a_strength, team_b_strength):

    diff = team_a_strength - team_b_strength

    probability = 0.5 + (diff / 200)

    probability = max(0.1, min(0.9, probability))

    if random.random() < probability:
        return "A"

    return "B"
