
from player import Player

TEAM_NAME = "AC Milan"
TEAM_ID = "ac_milan"
FORMATION = "3-4-2-1"

STARTING_XI = [
    {"role": "KL", "player": Player("Mike Maignan", "GK", 87)},
    {"role": "STP", "player": Player("Strahinja Pavlovic", "DEF", 78)},
    {"role": "STP", "player": Player("Mario Gila", "DEF", 79)},
    {"role": "STP", "player": Player("Koni De Winter", "DEF", 77)},
    {"role": "SLA", "player": Player("Diego Moreira", "DEF", 74)},
    {"role": "OS", "player": Player("Ardon Jashari", "MID", 78)},
    {"role": "OS", "player": Player("Adrien Rabiot", "MID", 83)},
    {"role": "SĞA", "player": Player("Alexis Saelemaekers", "MID", 80)},
    {"role": "OOS", "player": Player("Luka Modric", "MID", 85)},
    {"role": "OOS", "player": Player("Alphadjo Cisse", "MID", 70)},
    {"role": "SNT", "player": Player("Gonçalo Ramos", "FWD", 82)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
