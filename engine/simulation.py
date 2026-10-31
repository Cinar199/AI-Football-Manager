import random
import math


CARD_RATES = {
    "GK": {"yellow": 0.01, "red": 0.001, "injury": 0.01},
    "DEF": {"yellow": 0.12, "red": 0.02, "injury": 0.04},
    "MID": {"yellow": 0.09, "red": 0.012, "injury": 0.04},
    "FWD": {"yellow": 0.05, "red": 0.005, "injury": 0.03}
}


def get_players(team):
    return [item["player"] for item in team.STARTING_XI]


def get_team_ratings(team):
    players = get_players(team)

    def average(position):
        values = [p.ovr for p in players if p.position == position]
        return sum(values) / len(values) if values else 0

    gk = average("GK")
    defense = average("DEF")
    midfield = average("MID")
    attack = average("FWD")

    attacking = (
        attack * 0.50 + midfield * 0.35
        + defense * 0.10 + gk * 0.05
    )

    defending = (
        gk * 0.35 + defense * 0.40
        + midfield * 0.20 + attack * 0.05
    )

    return attacking, defending


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

    for p in players:
        multiplier = {
            "GK": 0.05,
            "DEF": 0.8,
            "MID": 2.5,
            "FWD": 5
        }.get(p.position, 1)

        weights.append(p.ovr * multiplier)

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
        "team": team.TEAM_NAME,
        "scorer": scorer.name,
        "assist": assist.name if assist else None
    }


def generate_disciplinary_events(team):
    events = []

    for player in get_players(team):
        rates = CARD_RATES.get(
            player.position,
            CARD_RATES["MID"]
        )

        if random.random() < rates["red"]:
            minute = random.randint(1, 90)

            events.append({
                "minute": minute,
                "type": "red_card",
                "team": team.TEAM_NAME,
                "player": player.name,
                "reason": "Doğrudan kırmızı kart"
            })

        else:
            if random.random() < rates["yellow"]:
                first_minute = random.randint(1, 85)

                events.append({
                    "minute": first_minute,
                    "type": "yellow_card",
                    "team": team.TEAM_NAME,
                    "player": player.name
                })

                if random.random() < 0.08:
                    second_minute = random.randint(
                        first_minute + 1, 90
                    )

                    events.append({
                        "minute": second_minute,
                        "type": "second_yellow",
                        "team": team.TEAM_NAME,
                        "player": player.name
                    })

                    events.append({
                        "minute": second_minute,
                        "type": "red_card",
                        "team": team.TEAM_NAME,
                        "player": player.name,
                        "reason": "İkinci sarı kart"
                    })

        if random.random() < rates["injury"]:
            events.append({
                "minute": random.randint(1, 90),
                "type": "injury",
                "team": team.TEAM_NAME,
                "player": player.name
            })

    return events


def red_card_impact(events, team_name):
    red_cards = [
        event for event in events
        if event["type"] == "red_card"
        and event["team"] == team_name
    ]

    impact = 0

    for card in red_cards:
        remaining_time = (90 - card["minute"]) / 90
        impact += remaining_time

    return impact


def simulate_match(home, away):
    events = []

    events.extend(generate_disciplinary_events(home))
    events.extend(generate_disciplinary_events(away))

    home_attack, home_defense = get_team_ratings(home)
    away_attack, away_defense = get_team_ratings(away)

    home_red_impact = red_card_impact(events, home.TEAM_NAME)
    away_red_impact = red_card_impact(events, away.TEAM_NAME)

    home_xg = (
        1.35 + (home_attack - away_defense) / 30 + 0.20
    )

    away_xg = (
        1.15 + (away_attack - home_defense) / 30
    )

    # Kırmızı kart etkisi
    home_xg *= max(0.35, 1 - home_red_impact * 0.30)
    away_xg *= max(0.35, 1 - away_red_impact * 0.30)

    # Rakibin gol beklentisinin artması
    home_xg += away_red_impact * 0.35
    away_xg += home_red_impact * 0.35

    home_xg = max(0.15, min(4.0, home_xg))
    away_xg = max(0.15, min(4.0, away_xg))

    home_goals = poisson(home_xg)
    away_goals = poisson(away_xg)

    for _ in range(home_goals):
        events.append(
            generate_goal(home, random.randint(1, 90))
        )

    for _ in range(away_goals):
        events.append(
            generate_goal(away, random.randint(1, 90))
        )

    events.sort(key=lambda event: event["minute"])

    return {
        "home": home.TEAM_NAME,
        "away": away.TEAM_NAME,
        "score": f"{home_goals}-{away_goals}",
        "home_xg": round(home_xg, 2),
        "away_xg": round(away_xg, 2),
        "events": events
    }
