
from player import Player

TEAM_NAME = "FK Zeyzella"
TEAM_ID = "fk_zeyzella"
FORMATION = "5-3-2"

STARTING_XI = [
    {"role": "KL", "player": Player("Wladimiro Falcone", "GK", 78)},
    {"role": "SLB", "player": Player("Oleksandr Zinchenko", "DEF", 79)},
    {"role": "STP", "player": Player("Tiago Gabriel", "DEF", 71)},
    {"role": "STP", "player": Player("Jan Bednarek", "DEF", 76)},
    {"role": "STP", "player": Player("Gaspar", "DEF", 72)},
    {"role": "SĞB", "player": Player("Tiago Santos", "DEF", 78)},
    {"role": "OS", "player": Player("Jurgen Ekkelenkamp", "MID", 76)},
    {"role": "OS", "player": Player("Ivan Ilić", "MID", 78)},
    {"role": "OS", "player": Player("Medon Berisha", "MID", 68)},
    {"role": "SNT", "player": Player("Willem Geubbels", "FWD", 70)},
    {"role": "SNT", "player": Player("Ange-Yoan Bonny", "FWD", 76)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
