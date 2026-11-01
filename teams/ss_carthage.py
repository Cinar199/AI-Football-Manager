
from player import Player

TEAM_NAME = "SS Carthage"
TEAM_ID = "ss_carthage"

FORMATION = "5-2-3"

STARTING_XI = [
    {"role": "KL", "player": Player("Kerem Matisli", "GK", 63)},

    {"role": "SLB", "player": Player("Delprato", "DEF", 75)},
    {"role": "STP", "player": Player("Martin Vitik", "DEF", 74)},
    {"role": "STP", "player": Player("Arseniy Batagov", "DEF", 75)},
    {"role": "STP", "player": Player("Diego Carlos", "DEF", 78)},
    {"role": "SĞB", "player": Player("Abdurrahman Üresin", "DEF", 65)},

    {"role": "DOS", "player": Player("Mandela Keita", "MID", 73)},
    {"role": "OS", "player": Player("Bitello", "MID", 78)},

    {"role": "SLK", "player": Player("El Bilal Toure", "FWD", 73)},
    {"role": "SNT", "player": Player("Endrick", "FWD", 77)},
    {"role": "SĞK", "player": Player("Ianis Hagi", "FWD", 72)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")

    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
