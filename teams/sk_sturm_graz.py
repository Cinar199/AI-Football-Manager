
from player import Player

TEAM_NAME = "SK Sturm Graz"
TEAM_ID = "sk_sturm_graz"
FORMATION = "4-1-4-1"

STARTING_XI = [
    {"role": "KL", "player": Player("Daniil Khudyakov", "GK", 70)},
    {"role": "SLB", "player": Player("Luis Balbo", "DEF", 68)},
    {"role": "STP", "player": Player("Joshua Quarshie", "DEF", 70)},
    {"role": "STP", "player": Player("Petar Petrovic", "DEF", 67)},
    {"role": "SĞB", "player": Player("Arjan Malic", "DEF", 70)},
    {"role": "DOS", "player": Player("Jon Gorenc Stankovic", "MID", 76)},
    {"role": "SLA", "player": Player("Simon Seidl", "MID", 69)},
    {"role": "OS", "player": Player("Luca Weinhandl", "MID", 65)},
    {"role": "OS", "player": Player("Otar Kiteishvili", "MID", 80)},
    {"role": "SĞA", "player": Player("Jacob Peter Hödl", "MID", 67)},
    {"role": "SNT", "player": Player("Omar Diakate", "FWD", 69)}
]


def show_team():
    print(f"\n{TEAM_NAME} - {FORMATION}")
    for item in STARTING_XI:
        player = item["player"]
        print(f'{item["role"]}: {player.name} | OVR: {player.ovr}')
      
