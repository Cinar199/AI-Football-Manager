
from player import Player

TEAM_NAME = "Ermis SC"
TEAM_ID = "ermis_sc"

FORMATION = "4-3-3"

STARTING_XI = [
    {"role": "KL", "player": Player("Elia Caprile", "GK", 78)},

    {"role": "SLB", "player": Player("Adam Obert", "DEF", 73)},
    {"role": "STP", "player": Player("Juan Rodriguez", "DEF", 71)},
    {"role": "STP", "player": Player("Raphael Kofler", "DEF", 67)},
    {"role": "SĞB", "player": Player("Omar El Hilali", "DEF", 75)},

    {"role": "MO", "player": Player("Alessandro Romano", "MID", 65)},
    {"role": "MO", "player": Player("Michel Adopo", "MID", 73)},
    {"role": "OOS", "player": Player("Daniel Maldini", "MID", 74)},

    {"role": "SLA", "player": Player("Kamaldeen Sulemana", "FWD", 73)},
    {"role": "SĞA", "player": Player("Johan Bakayoko", "FWD", 77)},
    {"role": "SNT", "player": Player("Yavuz Blanovič", "FWD", 84)},
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")

    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
