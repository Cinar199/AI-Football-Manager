
from player import Player

TEAM_NAME = "Ermis SC"
TEAM_ID = "ermis_sc"

FORMATION = "4-3-3"

STARTING_XI = [
    {"role": "KL", "player": Player("Elia Caprile", "GK", 78)},

    {"role": "SLB", "player": Player("Juan Rodriguez", "DEF", 71)},
    {"role": "STP", "player": Player("Berthel Askou", "DEF", 67)},
    {"role": "STP", "player": Player("Yerry Mina", "DEF", 76)},
    {"role": "SĞB", "player": Player("Omar El Hilali", "DEF", 75)},

    {"role": "MO", "player": Player("Alessandro Romano", "MID", 65)},
    {"role": "MO", "player": Player("Matteo Arda Balliistelli", "MID", 75)},
    {"role": "OOS", "player": Player("Daniel Maldini", "MID", 74)},

    {"role": "SLA", "player": Player("Kamaldeen Sulemana", "FWD", 73)},
    {"role": "SĞA", "player": Player("Johan Bakayoko", "FWD", 77)},
    {"role": "SNT", "player": Player("Yavuz Blanovič", "FWD", 84)},
]


SUBSTITUTES = [
    {
        "player": Player("Riyad Idrissi", "DEF", 68),
        "role": "SLB",
        "replaces": "Juan Rodriguez"
    },
    {
        "player": Player("Mitja Krizan", "DEF", 68),
        "role": "STP",
        "replaces": "Yerry Mina"
    },
    {
        "player": Player("Raphael Kofler", "DEF", 67),
        "role": "SĞB",
        "replaces": "Omar El Hilali"
    },
    {
        "player": Player("Hami Aslanovic", "MID", 70),
        "role": "MO",
        "replaces": "Alessandro Romano"
    },
    {
        "player": Player("Alieu Fadera", "FWD", 73),
        "role": "SLA",
        "replaces": "Kamaldeen Sulemana"
    }
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")

    print("\nİLK 11")
    for item in STARTING_XI:
        player = item["player"]
        print(
            f'{item["role"]}: {player.name} | OVR: {player.ovr}'
        )

    print("\nYEDEKLER")
    for item in SUBSTITUTES:
        player = item["player"]
        print(
            f'{player.name} | OVR: {player.ovr} '
            f'| Yerine: {item["replaces"]}'
        )
        
