
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from teams import (
    ssc_vincia,
    reale_vincia,
    ermis_sc,
    ss_carthage,
    juventus,
    as_roma,
    fk_zeyzella
)

from engine.simulation import simulate_match

app = FastAPI(
    title="AI Football Manager",
    version="1.4.0"
)

TEAMS = {
    "ssc_vincia": ssc_vincia,
    "reale_vincia": reale_vincia,
    "ermis_sc": ermis_sc,
    "ss_carthage": ss_carthage,
    "juventus": juventus,
    "as_roma": as_roma,
    "fk_zeyzella": fk_zeyzella
}


class MatchRequest(BaseModel):
    home: str
    away: str
    home_tactic: str = "dengeli"
    away_tactic: str = "dengeli"
    home_instruction: str = Field(default="", max_length=2000)
    away_instruction: str = Field(default="", max_length=2000)


def format_events(events):
    lines = []

    for event in events:
        minute = event["minute"]
        team = event["team"]
        player = event.get("player") or event.get("scorer", "Bilinmiyor")

        if event["type"] == "goal":
            assist = event.get("assist")
            line = f"⚽ {minute}' {player}"
            if assist:
                line += f" (Asist: {assist})"
        elif event["type"] == "yellow_card":
            line = f"🟨 {minute}' {player} - Sarı kart"
        elif event["type"] == "red_card":
            line = f"🟥 {minute}' {player} - Kırmızı kart"
        elif event["type"] == "second_yellow":
            line = f"🟨 {minute}' {player} - İkinci sarı kart"
        elif event["type"] == "injury":
            line = f"🚑 {minute}' {player} - Sakatlık"
        else:
            continue

        lines.append(f"**{line}** — {team}")

    return "\n".join(lines) if lines else "Maçta kayda değer olay yaşanmadı."


def validate_teams(home, away):
    if home not in TEAMS or away not in TEAMS:
        raise HTTPException(404, "Takım bulunamadı.")
    if home == away:
        raise HTTPException(400, "Takım kendisiyle oynayamaz.")


def prepare_match_result(result):
    result["formatted_events"] = format_events(result["events"])
    return result


@app.get("/")
def home():
    return {"project": "AI Football Manager", "status": "online"}


@app.get("/health")
def health():
    return {"online": True, "project": "AI Football Manager"}


@app.get("/teams")
def get_teams():
    return {
        "teams": [
            {
                "id": team_id,
                "name": team.TEAM_NAME,
                "formation": team.FORMATION
            }
            for team_id, team in TEAMS.items()
        ]
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
            {"role": item["role"], **item["player"].info()}
            for item in team.STARTING_XI
        ]
    }


@app.get("/match")
def play_match(home: str = "ssc_vincia", away: str = "reale_vincia"):
    validate_teams(home, away)
    result = simulate_match(TEAMS[home], TEAMS[away])
    return prepare_match_result(result)


@app.post("/match")
def play_custom_match(data: MatchRequest):
    validate_teams(data.home, data.away)

    if data.home_tactic.lower() not in ["defansif", "dengeli", "ofansif"]:
        raise HTTPException(400, "Geçersiz ev sahibi taktiği.")

    if data.away_tactic.lower() not in ["defansif", "dengeli", "ofansif"]:
        raise HTTPException(400, "Geçersiz deplasman taktiği.")

    result = simulate_match(
        TEAMS[data.home],
        TEAMS[data.away],
        home_tactic=data.home_tactic,
        away_tactic=data.away_tactic,
        home_instruction=data.home_instruction,
        away_instruction=data.away_instruction
    )

    return prepare_match_result(result)
    
