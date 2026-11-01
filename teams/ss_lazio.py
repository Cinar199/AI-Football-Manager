
from player import Player

TEAM_NAME = "SS Lazio"
TEAM_ID = "ss_lazio"
FORMATION = "4-2-3-1"

STARTING_XI = [
    {"role": "KL", "player": Player("Christos Mandas", "GK", 77)},
    {"role": "SLB", "player": Player("Nuno Tavares", "DEF", 79)},
    {"role": "STP", "player": Player("Oliver Provstgaard", "DEF", 73)},
    {"role": "STP", "player": Player("Danilho Doekhi", "DEF", 78)},
    {"role": "SĞB", "player": Player("Romano Floriani Mussolini", "DEF", 70)},
    {"role": "DOS", "player": Player("Nicolò Rovella", "MID", 80)},
    {"role": "DOS", "player": Player("Kenneth Taylor", "MID", 78)},
    {"role": "SLK", "player": Player("Mattia Zaccagni", "FWD", 81)},
    {"role": "OOS", "player": Player("Davide Frattesi", "MID", 82)},
    {"role": "SĞK", "player": Player("Gustav Isaksen", "FWD", 77)},
    {"role": "SNT", "player": Player("Andrea Pinamonti", "FWD", 78)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
  
