from player import Player

TEAM_NAME = "SSC Vincia"
TEAM_ID = "ssc_vincia"

FORMATION = "4-2-2-2"

STARTING_XI = [
    {"role": "KL", "player": Player("Alex Meret", "GK", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "SLB", "player": Player("Mathias Olivera", "DEF", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "STP", "player": Player("Lautaro Rivero", "DEF", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "STP", "player": Player("Sam Beukama", "DEF", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "SĞB", "player": Player("Kyriani Sabbe", "DEF", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "SLA", "player": Player("Noa Lang", "MID", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "OS", "player": Player("Kevin De Bruyne", "MID", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "OS", "player": Player("Scott McTominay", "MID", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "SĞA", "player": Player("David Neres", "MID", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "SNT", "player": Player("Rasmus Højlund", "FWD", 70, 70, 70, 70, 70, 70, 70)},
    {"role": "SNT", "player": Player("Yogi Neko", "FWD", 70, 70, 70, 70, 70, 70, 70)},
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
