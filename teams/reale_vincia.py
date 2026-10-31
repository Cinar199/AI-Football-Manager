
from player import Player

TEAM_NAME = "Reale Vincia FC"
TEAM_ID = "reale_vincia"

FORMATION = "3-4-1-2"

STARTING_XI = [
    {"role": "KL", "player": Player("Marco Carnesecchi", "GK", 86)},
    {"role": "STP", "player": Player("Giorgio Scalvini", "DEF", 79)},
    {"role": "STP", "player": Player("Isak Hien", "DEF", 79)},
    {"role": "STP", "player": Player("Oumar Solet", "DEF", 78)},
    {"role": "SLB", "player": Player("Lorenzo Bernasconi", "DEF", 71)},
    {"role": "OS", "player": Player("Éderson", "MID", 82)},
    {"role": "OS", "player": Player("Franck Kessié", "MID", 79)},
    {"role": "SĞB", "player": Player("Raoul Bellanova", "DEF", 78)},
    {"role": "OOS", "player": Player("Charles De Ketelaere", "MID", 81)},
    {"role": "SF", "player": Player("Giacomo Raspadori", "FWD", 78)},
    {"role": "SF", "player": Player("Gianluca Scamacca", "FWD", 78)},
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")

    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
