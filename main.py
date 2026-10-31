
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from teams import ssc_vincia, reale_vincia
from engine.simulation import simulate_match

app = FastAPI(
    title="AI Football Manager",
    version="1.1.0"
)

TEAMS = {
    "ssc_vincia": ssc_vincia,
    "reale_vincia": reale_vincia
}


class MatchRequest(BaseModel):
    home: str
    away: str

    home_tactic: str = "dengeli"
    away_tactic: str = "dengeli"

    home_instruction: str = Field(default="", max_length=2000)
    away_instruction: str = Field(default="", max_length=2000)


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


def validate_teams(home, away):
    if home not in TEAMS or away not in TEAMS:
        raise HTTPException(404, "Takım bulunamadı.")

    if home == away:
        raise HTTPException(400, "Takım kendisiyle oynayamaz.")


@app.get("/match")
def play_match(
    home: str = "ssc_vincia",
    away: str = "reale_vincia"
):
    validate_teams(home, away)

    return simulate_match(TEAMS[home], TEAMS[away])


@app.post("/match")
def play_custom_match(data: MatchRequest):
    validate_teams(data.home, data.away)

    if data.home_tactic.lower() not in [
        "defansif", "dengeli", "ofansif"
    ]:
        raise HTTPException(400, "Geçersiz ev sahibi taktiği.")

    if data.away_tactic.lower() not in [
        "defansif", "dengeli", "ofansif"
    ]:
        raise HTTPException(400, "Geçersiz deplasman taktiği.")

    return simulate_match(
        TEAMS[data.home],
        TEAMS[data.away],
        home_tactic=data.home_tactic,
        away_tactic=data.away_tactic,
        home_instruction=data.home_instruction,
        away_instruction=data.away_instruction
    )
    
