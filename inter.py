
from player import Player

TEAM_NAME = "Inter Milan"
TEAM_ID = "inter"
FORMATION = "3-5-2"

STARTING_XI = [
    {"role": "KL", "player": Player("Unai Simon", "GK", 86)},
    {"role": "STP", "player": Player("Yann Bisseck", "DEF", 80)},
    {"role": "STP", "player": Player("Manuel Akanji", "DEF", 84)},
    {"role": "STP", "player": Player("Alessandro Bastoni", "DEF", 87)},
    {"role": "SLA", "player": Player("Federico Dimarco", "DEF", 86)},
    {"role": "OS", "player": Player("Nicolò Barella", "MID", 87)},
    {"role": "OS", "player": Player("Petar Sucic", "MID", 78)},
    {"role": "OS", "player": Player("Curtis Jones", "MID", 80)},
    {"role": "SĞA", "player": Player("Djed Spence", "DEF", 77)},
    {"role": "SNT", "player": Player("Lautaro Martinez", "FWD", 88)},
    {"role": "SNT", "player": Player("Marcus Thuram", "FWD", 85)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
