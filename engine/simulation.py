
import random
import math


def get_team_ratings(team):
    players = [item["player"] for item in team.STARTING_XI]

    def average(position):
        selected = [p.ovr for p in players if p.position == position]
        return sum(selected) / len(selected) if selected else 0

    gk = average("GK")
    defense = average("DEF")
    midfield = average("MID")
    attack = average("FWD")

    attacking_power = (
        attack * 0.50 +
        midfield * 0.35 +
        defense * 0.10 +
        gk * 0.05
    )

    defensive_power = (
        gk * 0.35 +
        defense * 0.40 +
        midfield * 0.20 +
        attack * 0.05
    )

    return attacking_power, defensive_power


def poisson(expected_goals):
    limit = math.exp(-expected_goals)
    probability = 1
    goals = 0

    while probability > limit:
        goals += 1
        probability *= random.random()

    return goals - 1


def simulate_match(home, away):
    home_attack, home_defense = get_team_ratings(home)
    away_attack, away_defense = get_team_ratings(away)

    home_xg = 1.35 + (home_attack - away_defense) / 30 + 0.20
    away_xg = 1.15 + (away_attack - home_defense) / 30

    home_xg = max(0.15, min(4.0, home_xg))
    away_xg = max(0.15, min(4.0, away_xg))

    home_goals = poisson(home_xg)
    away_goals = poisson(away_xg)

    if home_goals > away_goals:
        result = "Ev sahibi kazandı"
    elif away_goals > home_goals:
        result = "Deplasman kazandı"
    else:
        result = "Berabere"

    return {
        "home": home.TEAM_NAME,
        "away": away.TEAM_NAME,
        "score": f"{home_goals}-{away_goals}",
        "home_xg": round(home_xg, 2),
        "away_xg": round(away_xg, 2),
        "result": result
    }
    
