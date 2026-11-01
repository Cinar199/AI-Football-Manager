
from player import Player

TEAM_NAME = "US Torino"
TEAM_ID = "us_torino"
FORMATION = "3-5-2"

STARTING_XI = [
    {"role": "KL", "player": Player("Lucas Perri", "GK", 79)},
    {"role": "STP", "player": Player("Pietro Comuzzo", "DEF", 76)},
    {"role": "STP", "player": Player("Saul Coco", "DEF", 76)},
    {"role": "STP", "player": Player("Ardian Ismajli", "DEF", 75)},
    {"role": "SLA", "player": Player("Alessio Cacciamani", "MID", 67)},
    {"role": "OS", "player": Player("Cesare Casadei", "MID", 76)},
    {"role": "OS", "player": Player("Gvidas Gineitis", "MID", 72)},
    {"role": "OS", "player": Player("Daniel Bragança", "MID", 77)},
    {"role": "SĞA", "player": Player("Zakaria Aboukhlal", "MID", 76)},
    {"role": "SNT", "player": Player("Giovanni Simeone", "FWD", 77)},
    {"role": "SNT", "player": Player("Che Adams", "FWD", 77)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
