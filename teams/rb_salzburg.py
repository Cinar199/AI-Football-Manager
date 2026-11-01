
from player import Player

TEAM_NAME = "RB Salzburg"
TEAM_ID = "rb_salzburg"
FORMATION = "4-1-4-1"

STARTING_XI = [
    {"role": "KL", "player": Player("Christian Zawieschitzky", "GK", 68)},
    {"role": "SLB", "player": Player("Dominik Schmid", "DEF", 70)},
    {"role": "STP", "player": Player("Kevin Boma", "DEF", 74)},
    {"role": "STP", "player": Player("Valentin Zabransky", "DEF", 67)},
    {"role": "SĞB", "player": Player("Nikolas Veratschnig", "DEF", 71)},
    {"role": "DOS", "player": Player("Soumaila Diabate", "MID", 72)},
    {"role": "SLA", "player": Player("Aboubacar Camara", "MID", 69)},
    {"role": "OS", "player": Player("Bartosz Mazurek", "MID", 70)},
    {"role": "OS", "player": Player("Abubakr Barry", "MID", 68)},
    {"role": "SĞA", "player": Player("Sota Kitano", "MID", 73)},
    {"role": "SNT", "player": Player("Karim Konate", "FWD", 77)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
