
from player import Player

TEAM_NAME = "ACF Fiorentina"
TEAM_ID = "acf_fiorentina"
FORMATION = "4-1-2-3"

STARTING_XI = [
    {"role": "KL", "player": Player("David De Gea", "GK", 84)},
    {"role": "SLB", "player": Player("Fabiano Parisi", "DEF", 76)},
    {"role": "STP", "player": Player("Radu Drăgușin", "DEF", 78)},
    {"role": "STP", "player": Player("Victor Valdepeñas", "DEF", 68)},
    {"role": "SĞB", "player": Player("Alex Jimenez", "DEF", 75)},
    {"role": "DOS", "player": Player("Cher Ndour", "MID", 73)},
    {"role": "OS", "player": Player("Christ Inao Oulai", "MID", 72)},
    {"role": "OS", "player": Player("Nicolò Fagioli", "MID", 78)},
    {"role": "SLK", "player": Player("Pedro Gonçalves", "FWD", 83)},
    {"role": "SNT", "player": Player("Mateo Pellegrino", "FWD", 75)},
    {"role": "SĞK", "player": Player("Franco Mastantuono", "FWD", 77)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
