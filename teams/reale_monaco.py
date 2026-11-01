
from player import Player

TEAM_NAME = "Reale Monaco"
TEAM_ID = "reale_monaco"
FORMATION = "4-2-3-1"

STARTING_XI = [
    {"role": "KL", "player": Player("Philipp Köhn", "GK", 76)},
    {"role": "SLB", "player": Player("Nazinho", "DEF", 72)},
    {"role": "STP", "player": Player("Christian Mawissa", "DEF", 77)},
    {"role": "STP", "player": Player("Sadibou Sane", "DEF", 73)},
    {"role": "SĞB", "player": Player("Vanderson", "DEF", 80)},
    {"role": "DOS", "player": Player("Denis Zakaria", "MID", 82)},
    {"role": "DOS", "player": Player("Lamine Camara", "MID", 78)},
    {"role": "SLK", "player": Player("Mathys Detourbet", "FWD", 68)},
    {"role": "OOS", "player": Player("Aleksandr Golovin", "MID", 83)},
    {"role": "SĞK", "player": Player("Ansu Fati", "FWD", 78)},
    {"role": "SNT", "player": Player("Folarin Balogun", "FWD", 80)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
