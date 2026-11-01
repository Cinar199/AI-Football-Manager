
from player import Player

TEAM_NAME = "Genoa CFC"
TEAM_ID = "genoa_cfc"
FORMATION = "3-4-2-1"

STARTING_XI = [
    {"role": "KL", "player": Player("J. Bijlow", "GK", 79)},
    {"role": "STP", "player": Player("J. Vasquez", "DEF", 77)},
    {"role": "STP", "player": Player("A. Marcandalli", "DEF", 70)},
    {"role": "STP", "player": Player("L. Ostigard", "DEF", 75)},
    {"role": "SLA", "player": Player("M. Mitaj", "DEF", 73)},
    {"role": "OS", "player": Player("M. Frendrup", "MID", 78)},
    {"role": "OS", "player": Player("D. Sow", "MID", 77)},
    {"role": "SĞA", "player": Player("C. Drameh", "DEF", 72)},
    {"role": "GF", "player": Player("S. El Shaarawy", "FWD", 77)},
    {"role": "SNT", "player": Player("Vitinha", "FWD", 77)},
    {"role": "GF", "player": Player("T. Baldanzi", "FWD", 77)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
