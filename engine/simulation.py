import random


def team_strength(team):
    players = [item["player"] for item in team.STARTING_XI]

    attack = sum(
        (p.sho + p.pac + p.dri) / 3
        for p in players
        if p.position == "FWD" or p.position == "MID"
    )

    defense = sum(
        (p.defending + p.phy + p.pac) / 3
        for p in players
        if p.position == "DEF"
    )

    return attack / 6, defense / 4


def simulate_match(home, away):
    home_attack, home_defense = team_strength(home)
    away_attack, away_defense = team_strength(away)

    home_chance = max(0.15, min(0.75,
        0.35 + (home_attack - away_defense) / 500
    ))

    away_chance = max(0.15, min(0.75,
        0.30 + (away_attack - home_defense) / 500
    ))

    home_goals = sum(
        1 for _ in range(12)
        if random.random() < home_chance
    )

    away_goals = sum(
        1 for _ in range(12)
        if random.random() < away_chance
    )

    return {
        "home": home.TEAM_NAME,
        "away": away.TEAM_NAME,
        "score": f"{home_goals}-{away_goals}"
    }
