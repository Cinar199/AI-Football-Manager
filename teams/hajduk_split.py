
from player import Player

TEAM_NAME = "Hajduk Split"
TEAM_ID = "hajduk_split"
FORMATION = "4-2-3-1"

STARTING_XI = [
    {"role": "KL", "player": Player("Toni Silic", "GK", 69)},
    {"role": "SLB", "player": Player("Simun Hrgovic", "DEF", 68)},
    {"role": "STP", "player": Player("Dario Maresic", "DEF", 73)},
    {"role": "STP", "player": Player("Dennis Hadzukadunic", "DEF", 74)},
    {"role": "SĞB", "player": Player("Luka Hodak", "DEF", 67)},
    {"role": "DOS", "player": Player("Leander Dendoncker", "MID", 76)},
    {"role": "DOS", "player": Player("Adrion Pajaziti", "MID", 70)},
    {"role": "SLK", "player": Player("Michele Sego", "FWD", 71)},
    {"role": "OOS", "player": Player("Dalisson de Almeide", "MID", 69)},
    {"role": "SĞK", "player": Player("Carlos Martin", "FWD", 73)},
    {"role": "SNT", "player": Player("Marko Livaja", "FWD", 78)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
