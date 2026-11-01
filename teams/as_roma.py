
from player import Player

TEAM_NAME = "AS Roma"
TEAM_ID = "as_roma"
FORMATION = "4-2-3-1"

STARTING_XI = [
    {"role": "KL", "player": Player("Mile Svilar", "GK", 84)},
    {"role": "SLB", "player": Player("Nahuel Molina", "DEF", 80)},
    {"role": "STP", "player": Player("Gianluca Mancini", "DEF", 84)},
    {"role": "STP", "player": Player("Evan N'Dicka", "DEF", 81)},
    {"role": "SĞB", "player": Player("Wesley", "DEF", 79)},
    {"role": "DOS", "player": Player("Manu Koné", "MID", 80)},
    {"role": "DOS", "player": Player("Niccolò Pisilli", "MID", 74)},
    {"role": "SLK", "player": Player("Rodrigo Mora", "FWD", 77)},
    {"role": "OOS", "player": Player("Paulo Dybala", "MID", 85)},
    {"role": "SĞK", "player": Player("Matías Soulé", "FWD", 79)},
    {"role": "SNT", "player": Player("Donyell Malen", "FWD", 80)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
