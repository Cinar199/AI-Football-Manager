
from player import Player

TEAM_NAME = "FC Basel"
TEAM_ID = "fc_basel"
FORMATION = "4-2-2-2"

STARTING_XI = [
    {"role": "KL", "player": Player("Jonas Omlin", "GK", 76)},
    {"role": "SLB", "player": Player("Coleen Louis", "DEF", 67)},
    {"role": "STP", "player": Player("Flavius Daniliuc", "DEF", 74)},
    {"role": "STP", "player": Player("Akpe Victory", "DEF", 68)},
    {"role": "SĞB", "player": Player("Keigo Tsunemoto", "DEF", 73)},
    {"role": "DOS", "player": Player("Metinho", "MID", 72)},
    {"role": "DOS", "player": Player("Gabriel Sigua", "MID", 70)},
    {"role": "SLA", "player": Player("Philip Otele", "FWD", 75)},
    {"role": "SĞA", "player": Player("Xherdan Shaqiri", "MID", 79)},
    {"role": "SNT", "player": Player("Giacomo Koloto", "FWD", 68)},
    {"role": "SNT", "player": Player("Zan Celar", "FWD", 74)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
