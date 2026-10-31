
from fastapi import FastAPI, HTTPException

from teams import ssc_vincia, reale_vincia
from engine.simulation import simulate_match

app = FastAPI(
    title="AI Football Manager",
    version="1.0.0"
)

TEAMS = {
    "ssc_vincia": ssc_vincia,
    "reale_vincia": reale_vincia
}


@app.get("/")
def home():
    return {
        "project": "AI Football Manager",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "online": True,
        "project": "AI Football Manager"
    }


@app.get("/team/{team_id}")
def get_team(team_id: str):
    if team_id not in TEAMS:
        raise HTTPException(404, "Takım bulunamadı.")

    team = TEAMS[team_id]

    return {
        "name": team.TEAM_NAME,
        "formation": team.FORMATION,
        "players": [
            {
                "role": item["role"],
                **item["player"].info()
            }
            for item in team.STARTING_XI
        ]
    }


@app.get("/match")
def play_match(
    home: str = "ssc_vincia",
    away: str = "reale_vincia"
):
    if home not in TEAMS or away not in TEAMS:
        raise HTTPException(404, "Takım bulunamadı.")

    if home == away:
        raise HTTPException(400, "Takım kendisiyle oynayamaz.")

    return simulate_match(TEAMS[home], TEAMS[away])
