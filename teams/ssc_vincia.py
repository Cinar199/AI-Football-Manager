from player import Player

TEAM_NAME = "SSC Vincia"
TEAM_ID = "ssc_vincia"

FORMATION = "4-4-2"

STARTING_XI = [
    {"role": "KL", "player": Player("Alex Meret", "GK", 81)},
    {"role": "SLB", "player": Player("Mathias Olivera", "DEF", 77)},
    {"role": "STP", "player": Player("Lautaro Rivero", "DEF", 76)},
    {"role": "STP", "player": Player("Sam Beukama", "DEF", 78)},
    {"role": "SĞB", "player": Player("Kyriani Sabbe", "DEF", 75)},
    {"role": "SLA", "player": Player("Noa Lang", "MID", 79)},
    {"role": "OS", "player": Player("Kevin De Bruyne", "MID", 85)},
    {"role": "OS", "player": Player("Scott McTominay", "MID", 86)},
    {"role": "SĞA", "player": Player("David Neres", "MID", 81)},
    {"role": "SNT", "player": Player("Rasmus Højlund", "FWD", 78)},
    {"role": "SNT", "player": Player("Yogi Neko", "FWD", 75)},
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")

    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
