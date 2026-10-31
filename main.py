
import random
import math


def get_players(team):
    return [item["player"] for item in team.STARTING_XI]


def get_team_ratings(team):
    players = get_players(team)

    gk = [p.ovr for p in players if p.position == "GK"]
    defense = [p.ovr for p in players if p.position == "DEF"]
    midfield = [p.ovr for p in players if p.position == "MID"]
    attack = [p.ovr for p in players if p.position == "FWD"]

    def avg(values):
        return sum(values) / len(values) if values else 0

    return (
        avg(attack) * 0.50 + avg(midfield) * 0.35
        + avg(defense) * 0.10 + avg(gk) * 0.05,
        avg(gk) * 0.35 + avg(defense) * 0.40
        + avg(midfield) * 0.20 + avg(attack) * 0.05
    )


def poisson(expected_goals):
    limit = math.exp(-expected_goals)
    probability = 1
    goals = 0

    while probability > limit:
        goals += 1
        probability *= random.random()

    return goals - 1


def choose_scorer(team):
    players = get_players(team)
    weights = []

    for player in players:
        if player.position == "FWD":
            weight = 5
        elif player.position == "MID":
            weight = 2.5
        elif player.position == "DEF":
            weight = 0.8
        else:
            weight = 0.05

        weights.append(weight * player.ovr)

    return random.choices(players, weights=weights, k=1)[0]


def choose_assist(team, scorer):
    players = [
        p for p in get_players(team)
        if p != scorer and p.position != "GK"
    ]

    if not players:
        return None

    weights = [
        p.ovr * (2 if p.position == "MID" else 1)
        for p in players
    ]

    return random.choices(players, weights=weights, k=1)[0]


def generate_goal(team, minute):
    scorer = choose_scorer(team)
    assist = choose_assist(team, scorer)

    return {
        "minute": minute,
        "type": "goal",
        "scorer": scorer.name,
        "assist": assist.name if assist else None,
        "team": team.TEAM_NAME
    }


def simulate_match(home, away):
    home_attack, home_defense = get_team_ratings(home)
    away_attack, away_defense = get_team_ratings(away)

    home_xg = max(0.15, min(4.0,
        1.35 + (home_attack - away_defense) / 30 + 0.20
    ))

    away_xg = max(0.15, min(4.0,
        1.15 + (away_attack - home_defense) / 30
    ))

    home_goals = poisson(home_xg)
    away_goals = poisson(away_xg)

    events = []

    for _ in range(home_goals):
        events.append(generate_goal(home, random.randint(1, 90)))

    for _ in range(away_goals):
        events.append(generate_goal(away, random.randint(1, 90)))

    events.sort(key=lambda event: event["minute"])

    return {
        "home": home.TEAM_NAME,
        "away": away.TEAM_NAME,
        "score": f"{home_goals}-{away_goals}",
        "home_xg": round(home_xg, 2),
        "away_xg": round(away_xg, 2),
        "events": events
    }
    
