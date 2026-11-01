
from player import Player

TEAM_NAME = "Juventus"
TEAM_ID = "juventus"
FORMATION = "4-2-3-1"

STARTING_XI = [
    {"role": "KL", "player": Player("Guglielmo Vicario", "GK", 84)},
    {"role": "SLB", "player": Player("Andrea Cambiaso", "DEF", 79)},
    {"role": "STP", "player": Player("Nico Schlotterbeck", "DEF", 85)},
    {"role": "STP", "player": Player("Bremer", "DEF", 85)},
    {"role": "SĞB", "player": Player("Zeki Çelik", "DEF", 78)},
    {"role": "DOS", "player": Player("Pablo Barrios", "MID", 82)},
    {"role": "DOS", "player": Player("Khéphren Thuram", "MID", 81)},
    {"role": "SLK", "player": Player("Kenan Yıldız", "FWD", 79)},
    {"role": "OOS", "player": Player("Gilberto Mora", "MID", 73)},
    {"role": "SĞK", "player": Player("Francisco Conceição", "FWD", 79)},
    {"role": "SNT", "player": Player("Nick Woltemade", "FWD", 78)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
